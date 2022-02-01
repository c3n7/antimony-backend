from rest_framework import serializers
from .models import Msg


class MsgSerializer(serializers.ModelSerializer):
    sender_first_name = serializers.ReadOnlyField(
        source='user_from.first_name')
    sender_last_name = serializers.ReadOnlyField(source='user_from.last_name')

    class Meta:
        model = Msg
        fields = (
            'id',
            'message',
            'user_from',
            'sender_first_name',
            'sender_last_name',
            'user_to',
            'created_at',
        )


class MsgConversationSerializer(serializers.ModelSerializer):
    sender_first_name = serializers.ReadOnlyField(
        source='user_from.first_name')
    sender_last_name = serializers.ReadOnlyField(source='user_from.last_name')
    recepient_first_name = serializers.ReadOnlyField(
        source='user_to.first_name')
    recepient_last_name = serializers.ReadOnlyField(
        source='user_to.last_name')

    class Meta:
        model = Msg
        fields = (
            'id',
            'message',
            'user_from',
            'sender_first_name',
            'sender_last_name',
            'recepient_first_name',
            'recepient_last_name',
            'user_to',
            'created_at',
        )


class MsgCountSerializer(serializers.Serializer):
    dcount = serializers.IntegerField()
    user_from = serializers.IntegerField()
