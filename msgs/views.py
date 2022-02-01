from django.db.models import Count, Max
from rest_framework import viewsets, permissions, filters, generics
from filters.mixins import (
    FiltersMixin,
)

from .models import Msg
from .permissions import IsSenderOrRecepient
from .serializers import MsgSerializer, MsgCountSerializer


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
