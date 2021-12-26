from rest_framework.routers import SimpleRouter

from .views import MsgViewSet

router = SimpleRouter()
router.register(
    'msgs', MsgViewSet,
    basename='msgs'
)

urlpatterns = router.urls
