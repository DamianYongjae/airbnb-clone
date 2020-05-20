from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command tells me he loves me"
    print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times to you want me to tell you?"
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            print("i love you")
