from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'owner',
            'target',
            'first_name',
            'last_name',
            'created_at',
            'updated_at',
        )
