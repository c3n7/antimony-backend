from django.contrib.auth import get_user_model
from django.db import models


class Msg(models.Model):
    message = models.TextField()
    user_id = models.OneToOneField(
        get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
