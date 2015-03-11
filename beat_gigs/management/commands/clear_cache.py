from django.core.management.base import BaseCommand
from django.core.cache import caches

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        caches['wham_web_request'].clear()
        self.stdout.write('Cleared cache\n')