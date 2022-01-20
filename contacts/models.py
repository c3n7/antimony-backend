from django.contrib.auth import get_user_model
from django.db import models


class Contact(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, related_name="contact_owner")
    target = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, related_name="contact_target")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
