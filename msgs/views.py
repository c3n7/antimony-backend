from rest_framework import viewsets, permissions

from .models import Msg
from .permissions import IsSenderOrRecepient
from .serializers import MsgSerializer


class MsgViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsSenderOrRecepient,)
    queryset = Msg.objects.all()
    serializer_class = MsgSerializer
