from rest_framework import viewsets, permissions, filters
from filters.mixins import (
    FiltersMixin,
)

from .models import Msg
from .permissions import IsSenderOrRecepient
from .serializers import MsgSerializer


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
