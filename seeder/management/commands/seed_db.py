from django.core.management.base import BaseCommand
from users.seeder import seed as seed_users


class Command(BaseCommand):
    help = 'seed database'

    def handle(self, *args, **options):
        inserted = seed_users(200)
        print(inserted)
