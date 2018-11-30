from django.core.management.base import BaseCommand, CommandError
from shortener.models import UrlShort


class Command(BaseCommand):
    help = 'Refreshes all Url Shortener shortcodes'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        return UrlShort.objects.refresh_shortcodes()
