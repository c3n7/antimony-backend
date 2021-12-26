import sys
import io

from django_seed import Seed
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


def seed(count):
    seeder = Seed.seeder()

    # https://stackoverflow.com/a/29423946/7450617
    fields = get_user_model()._meta.get_fields()
    # print(fields)

    seeder.add_entity(get_user_model(), count, {
        "is_staff": False,
        "is_superuser": False,
        "is_active": True,
        "password": make_password("password"),
    })

    # HACK: deal with groups and user_permissions better
    # https://stackoverflow.com/a/1218951/7450617
    # hide the groups and user_permissions warnings
    old_syserr = sys.stderr
    my_stderr = io.StringIO()
    sys.stderr = my_stderr

    inserted_pks = seeder.execute()

    sys.stderr = old_syserr

    return inserted_pks
