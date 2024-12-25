# src/apps/feeds/management/commands/create_mock_categories.py
from django.core.management.base import BaseCommand
from apps.feeds.factories import CategoryFactory  # Adjust the import path if needed


class Command(BaseCommand):
    help = "Generate mock category data using Factory Boy"

    def add_arguments(self, parser):
        parser.add_argument(
            "--num_categories",
            type=int,
            default=10,
            help="Number of categories to create",
        )

    def handle(self, *args, **kwargs):
        num_categories = kwargs["num_categories"]
        for _ in range(num_categories):
            CategoryFactory.create()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {num_categories} categories")
        )
