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

        user = get_user_model().create_user(
            email=user_email,
            username=user_email,
            password=user_password,
        )

        self.stdout.write(
            self.style.SUCCESS('Successfully created user "%s"', user.email)
        )