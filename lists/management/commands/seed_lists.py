import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as lists_models
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This command create many lists"
    # print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many lists do you want to create?",
        )

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()

        all_user = user_models.User.objects.all()
        all_room = room_models.Room.objects.all()

        seeder.add_entity(
            lists_models.List, number, {"user": lambda x: random.choice(all_user),},
        )

        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        for pk in cleaned:
            list_model = lists_models.List.objects.get(pk=pk)
            to_add = all_room[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} lists created!"))
