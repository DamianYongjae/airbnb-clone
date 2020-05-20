import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations import models as reservations_models
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This command create many reservations"
    # print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many reservations do you want to create?",
        )

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()

        all_user = user_models.User.objects.all()
        all_room = room_models.Room.objects.all()

        seeder.add_entity(
            reservations_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "canceled", "confirmed"]),
                "room": lambda x: random.choice(all_room),
                "guest": lambda x: random.choice(all_user),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: (
                    datetime.now() + timedelta(days=random.randint(3, 25))
                ),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} reservations created!"))
