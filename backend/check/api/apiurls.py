from rest_framework.routers import DefaultRouter

from .viewsets import CheckViewSet, CheckHistoryViewSet

router = DefaultRouter()
router.register("check", CheckViewSet, basename="check")
router.register("history", CheckHistoryViewSet, basename="history")

urlpatterns = [
    *router.urls,
]
