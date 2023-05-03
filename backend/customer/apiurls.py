from rest_framework.routers import DefaultRouter

from .viewsets import AvatarViewSet, NoteViewSet, DriverLicenceViewSet, CustomerViewSet

router = DefaultRouter()
router.register("customer", CustomerViewSet, basename="customer")
router.register("avatar", AvatarViewSet, basename="avatar")
router.register("note", NoteViewSet, basename="note")
router.register("passport", DriverLicenceViewSet, basename="passport")

urlpatterns = [*router.urls]
