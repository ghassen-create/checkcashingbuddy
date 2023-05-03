from rest_framework.routers import DefaultRouter

from .viewsets import RegistrationViewSet, LoginViewSet, RefreshViewSet, GroupViewSet, PermissionViewSet, UserViewSet

router = DefaultRouter()
router.register("auth/register", RegistrationViewSet, basename="register")
router.register("auth/login", LoginViewSet, basename="login")
router.register("auth/refresh", RefreshViewSet, basename="refresh")
router.register("auth/group", GroupViewSet, basename="group")
router.register("auth/permission", PermissionViewSet, basename="permission")
router.register("user", UserViewSet, basename="user")

urlpatterns = [
    *router.urls,
]
