from django_seed import Seed
from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import Msg


class MsgSeeder:
    def gen_user(self, seeder, user_ids):
        # print(user_ids)
        user_id = seeder.faker.random_elements(
            user_ids, length=1, unique=False)

        user_id = user_id[0]
        user = get_user_model().objects.get(id=user_id)

        return user

    def gen_date_time(self, seeder):
        rand_datetime = seeder.faker.date_time_between(start_date='-4y')
        current_tz = timezone.get_current_timezone()
        timezoned_dt = timezone.make_aware(rand_datetime, current_tz)
        return timezoned_dt

    def seed(self, count):
        seeder = Seed.seeder()

        users = get_user_model().objects.values_list('id', flat=True)
        users = list(users)

        seeder.add_entity(Msg, count, {
            'user_from': lambda x: self.gen_user(seeder, users),
            'user_to': lambda x: self.gen_user(seeder, users),
            'message': lambda x: seeder.faker.paragraph(nb_sentences=5, variable_nb_sentences=False),
            'created_at': lambda x: self.gen_date_time(seeder),
        })

        inserted_pks = seeder.execute()
        return inserted_pks
