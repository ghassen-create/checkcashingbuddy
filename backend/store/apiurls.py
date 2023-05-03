from rest_framework.routers import DefaultRouter

from .viewsets import StoreViewSet

router = DefaultRouter()
router.register("store", StoreViewSet, basename="store")


urlpatterns = [*router.urls]
