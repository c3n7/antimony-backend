from rest_framework import serializers
from .models import Msg


class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Msg
        fields = (
            'id',
            'message',
            'user_from',
            'user_to',
            'created_at',
        )


class MsgCountSerializer(serializers.Serializer):
    dcount = serializers.IntegerField()
    # user_to = serializers.ModelField(
    #     model_field=Msg()._meta.get_field('user_to'))
    user_to = serializers.IntegerField()

    class Meta:
        # model = Msg
        fields = (
            'user_to',
            'dcount',
        )
