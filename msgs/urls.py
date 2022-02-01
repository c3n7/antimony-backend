from rest_framework.routers import SimpleRouter
from django.urls import path

from .views import MsgViewSet, MsgCountListView

router = SimpleRouter()
router.register(
    '', MsgViewSet,
    basename='msgs'
)

urlpatterns = [
    path('received-count/', MsgCountListView.as_view(),
         name="received-message-count"),
]
urlpatterns += router.urls
