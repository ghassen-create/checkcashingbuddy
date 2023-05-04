from rest_framework.routers import DefaultRouter

from .viewsets import CheckViewSet, CheckLogsViewSet

router = DefaultRouter()
router.register("check", CheckViewSet, basename="check")
router.register("history", CheckLogsViewSet, basename="history")

urlpatterns = [
    *router.urls,
]
