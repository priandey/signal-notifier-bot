from django.db import models
from core.models.signal_group import SignalGroup
from core.models.signal_user import SignalUser


class SignalMessage(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "target_group",
                    "source_user",
                    "target_user",
                    "received_at"
                ],
                name="unique_together_group_user_received"
            ),
            models.CheckConstraint(
                check=(
                    models.Q(
                        models.Q(
                            models.Q(target_user__isnull=False) & models.Q(target_group__isnull=True)
                        )
                        | models.Q(
                            models.Q(target_user__isnull=True) & models.Q(target_group__isnull=False)
                        )
                    )
                ),
                name="only_one_target_allowed",
                violation_error_message="Only one of target_group and target_user field can be set"
            ),
        ]

    target_group = models.ForeignKey(
        to=SignalGroup,
        verbose_name="Source Group",
        null=True,
        related_name="received_messages",
        on_delete=models.PROTECT,
    )

    target_user = models.ForeignKey(
        to=SignalUser,
        verbose_name="Source User",
        null=True,
        related_name="received_messages",
        on_delete=models.PROTECT,
    )

    source_user = models.ForeignKey(
        to=SignalUser,
        verbose_name="Source User",
        related_name="sent_messages",
        on_delete=models.PROTECT,
    )

    text_content = models.TextField(
        verbose_name="Text content",
    )

    raw_content = models.JSONField(
        verbose_name="Raw content",
        null=True
    )
    is_incoming = models.BooleanField(
        verbose_name="Is incoming",
    )

    received_at = models.DateTimeField(verbose_name="Message received at")

    created_at = models.DateTimeField(verbose_name="Model created at", auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name="Model modified at", auto_now=True)
