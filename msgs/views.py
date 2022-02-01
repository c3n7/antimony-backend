from django.db.models import Count
from rest_framework import viewsets, permissions, filters, generics
from filters.mixins import (
    FiltersMixin,
)

from .models import Msg
from .permissions import IsSenderOrRecepient
from .serializers import MsgSerializer, MsgCountSerializer, MsgConversationSerializer


class MsgViewSet(FiltersMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsSenderOrRecepient,)
    serializer_class = MsgSerializer

    # queryset = Msg.objects.all()
    def get_queryset(self):
        user = self.request.user
        queryset = Msg.objects.filter(
            user_from=user) | Msg.objects.filter(user_to=user)
        return queryset.order_by('id')

    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        'id': 'id',
        'user_from': 'user_from',
        'user_to': 'user_to',
    }


class MsgConversationListView(FiltersMixin, generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsSenderOrRecepient,)
    serializer_class = MsgConversationSerializer

    def get_queryset(self):
        conversation_with = self.request.query_params.get('with')

        if conversation_with is None:
            return Msg.objects.none()

        user = self.request.user
        queryset = Msg.objects.filter(
            user_from=user) | Msg.objects.filter(user_to=user)

        queryset = queryset.filter(user_from=conversation_with) | queryset.filter(
            user_to=conversation_with)
        return queryset.order_by('created_at')

    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        'id': 'id',
        'user_from': 'user_from',
        'user_to': 'user_to',
    }


class MsgCountListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MsgCountSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Msg.objects.filter(
            user_from=user) | Msg.objects.filter(user_to=user)
        return queryset.values('user_from').annotate(dcount=Count('user_from')).order_by('user_from')


class MsgLatestListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MsgSerializer

    def get_queryset(self):
        user = self.request.user
        # Get only messages sent to logged in user
        queryset = Msg.objects.filter(user_to=user)
        # return queryset.values('user_to').annotate(Count('user_to'), latest_msg=Max('created_at')).order_by('user_to')
        queryset = queryset.order_by(
            'user_from', '-created_at').distinct('user_from')
        return queryset
