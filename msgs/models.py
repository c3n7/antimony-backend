from django.contrib.auth import get_user_model
from django.db import models


class Msg(models.Model):
    message = models.TextField()
    user_from = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, related_name="msg_sender")
    # TODO: Find a way to ensure the from and to are not equal
    user_to = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, related_name="msg_target")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} to {}".format(self.user_from.id, self.user_to.id)
