from rest_framework import viewsets, permissions, filters
from filters.mixins import (
    FiltersMixin,
)

from .models import Msg
from .permissions import IsSenderOrRecepient
from .serializers import MsgSerializer


class MsgViewSet(FiltersMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsSenderOrRecepient,)
    queryset = Msg.objects.all()
    serializer_class = MsgSerializer

    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        'id': 'id',
        'user_from': 'user_from',
        'user_to': 'user_to',
    }
