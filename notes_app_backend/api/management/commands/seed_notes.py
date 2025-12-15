from django.core.management.base import BaseCommand
from api.models import Note


class Command(BaseCommand):
    help = "Seed the database with sample notes"

    # PUBLIC_INTERFACE
    def handle(self, *args, **options):
        """Create a few sample notes for development/demo."""
        samples = [
            {"title": "Welcome", "content": "This is your first note."},
            {"title": "Todo", "content": "1. Build API\n2. Test API\n3. Ship"},
        ]
        created = 0
        for s in samples:
            obj, was_created = Note.objects.get_or_create(title=s["title"], defaults={"content": s["content"]})
            created += 1 if was_created else 0
        self.stdout.write(self.style.SUCCESS(f"Seed complete. Created {created} notes."))
