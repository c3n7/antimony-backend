from rest_framework import viewsets, permissions, filters
from filters.mixins import (
    FiltersMixin,
)

from .models import Contact
from .permissions import IsOwner
from .serializers import ContactSerializer


class ContactViewSet(FiltersMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    serializer_class = ContactSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Contact.objects.filter(owner=user)
        return queryset.order_by('id')

    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        'id': 'id',
        'owner': 'owner',
        'target': 'target',
    }
