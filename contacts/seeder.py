from django_seed import Seed
from django.contrib.auth import get_user_model

from .models import Contact


class ContactSeeder:
    def gen_user(self, seeder, user_ids):
        # print(user_ids)
        user_id = seeder.faker.random_elements(
            user_ids, length=1, unique=False)

        user_id = user_id[0]
        user = get_user_model().objects.get(id=user_id)

        return user

    def seed(self, count):
        seeder = Seed.seeder()

        users = get_user_model().objects.values_list('id', flat=True)
        users = list(users)

        seeder.add_entity(Contact, count, {
            'owner': lambda x: self.gen_user(seeder, users),
            'target': lambda x: self.gen_user(seeder, users),
        })

        inserted_pks = seeder.execute()
        return inserted_pks
