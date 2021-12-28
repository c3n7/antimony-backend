from django_seed import Seed
from django.contrib.auth import get_user_model

from .models import Msg


class MsgSeeder:
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

        seeder.add_entity(Msg, count, {
            'user_from': lambda x: self.gen_user(seeder, users),
            'user_to': lambda x: self.gen_user(seeder, users),
            'message': lambda x: seeder.faker.paragraph(nb_sentences=5, variable_nb_sentences=False),
        })

        inserted_pks = seeder.execute()
        return inserted_pks
