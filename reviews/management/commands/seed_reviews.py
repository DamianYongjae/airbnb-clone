import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from reviews import models as reviews_model
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This command create many reviews"
    # print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many reviews do you want to create?",
        )

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()

        all_user = user_models.User.objects.all()
        all_room = room_models.Room.objects.all()

        seeder.add_entity(
            reviews_model.Review,
            number,
            {
                "accuracy": lambda x: random.randint(0, 5),
                "communication": lambda x: random.randint(0, 5),
                "cleanliness": lambda x: random.randint(0, 5),
                "location": lambda x: random.randint(0, 5),
                "check_in": lambda x: random.randint(0, 5),
                "value": lambda x: random.randint(0, 5),
                "room": lambda x: random.choice(all_room),
                "user": lambda x: random.choice(all_user),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
