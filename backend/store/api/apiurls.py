from rest_framework.routers import DefaultRouter

from .viewsets import StoreViewSet, StoreCustomerViewSet

router = DefaultRouter()
router.register("store", StoreViewSet, basename="store")
router.register("storecustomer", StoreCustomerViewSet, basename="storecustomer")


urlpatterns = [*router.urls]
