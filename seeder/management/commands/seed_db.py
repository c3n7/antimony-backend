from django.core.management.base import BaseCommand
from users.seeder import seed as seed_users
from msgs.seeder import MsgSeeder
from contacts.seeder import ContactSeeder


class Command(BaseCommand):
    help = 'seed database'

    def handle(self, *args, **options):
        inserted = seed_users(50)
        print(inserted)

        sd = ContactSeeder()
        inserted = sd.seed(1500)
        print(inserted)

        sd = MsgSeeder()
        inserted = sd.seed(10_000)
        print(inserted)
