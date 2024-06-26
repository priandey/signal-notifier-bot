import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create an admin user from environment"

    def handle(self, *args, **options):
        user_email = os.getenv("ADMIN_EMAIL")
        if user_email is None:
            raise CommandError("No `ADMIN_EMAIL` found in environment")

        user_password = os.getenv("ADMIN_PASSWORD")
        if user_password is None:
            raise CommandError("No `ADMIN_PASSWORD` found in environment")

        user, _created = get_user_model().objects.update_or_create(
            username=user_email,
            email=user_email,
            defaults={
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            }
        )

        user.set_password(user_password)
        user.save()

        self.stdout.write(
            self.style.SUCCESS(f'Successfully {"created" if _created else "updated"} user "{user.email}"')
        )
