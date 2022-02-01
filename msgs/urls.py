from rest_framework.routers import SimpleRouter
from django.urls import path

from .views import MsgViewSet, MsgCountListView, MsgLatestListView, MsgConversationListView

router = SimpleRouter()
router.register(
    '', MsgViewSet,
    basename='msgs'
)

urlpatterns = [
    path('received-count/', MsgCountListView.as_view(),
         name="received-message-count"),
    path('head/', MsgLatestListView.as_view(),
         name="received-head"),
    path('conversation/', MsgConversationListView.as_view(),
         name="conversation"),
]
urlpatterns += router.urls
