from django.core.management.base import BaseCommand
from rooms.models import Facility

# python manage.py seed_facilities
class Command(BaseCommand):
    help = "This command tells me that Facilities"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            if not Facility.objects.filter(name=f):
                Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))