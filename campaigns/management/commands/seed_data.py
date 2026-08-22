from django.core.management.base import BaseCommand

from campaigns.models import Campaign
from engagement.models import Donation
from engagement.models import VolunteerApplication


class Command(BaseCommand):

    help = "Seed demo data"

    def handle(self, *args, **kwargs):

        Campaign.objects.all().delete()

        campaign1 = Campaign.objects.create(
            title="Clean Water Drive",
            description="Providing clean drinking water to rural communities.",
            location="Prayagraj",
            target_amount=50000,
            start_date="2026-01-01",
            end_date="2026-12-31"
        )

        campaign2 = Campaign.objects.create(
            title="Education For All",
            description="Supporting education for underprivileged children.",
            location="Lucknow",
            target_amount=100000,
            start_date="2026-01-01",
            end_date="2026-12-31"
        )

        campaign3 = Campaign.objects.create(
            title="Food Distribution Camp",
            description="Distributing food kits to families in need.",
            location="Varanasi",
            target_amount=75000,
            start_date="2026-01-01",
            end_date="2026-12-31"
        )

        VolunteerApplication.objects.create(
            name="Rahul Sharma",
            email="rahul@example.com",
            phone="9876543210",
            skills="Event Management",
            campaign=campaign1
        )

        VolunteerApplication.objects.create(
            name="Ananya Singh",
            email="ananya@example.com",
            phone="9876543211",
            skills="Teaching",
            campaign=campaign2
        )

        Donation.objects.create(
            name="Amit Kumar",
            email="amit@example.com",
            amount=2000,
            campaign=campaign1
        )

        Donation.objects.create(
            name="Priya Verma",
            email="priya@example.com",
            amount=5000,
            campaign=campaign2
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Demo data inserted successfully."
            )
        )