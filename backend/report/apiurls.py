from rest_framework.routers import DefaultRouter

from .viewsets import ReportViewSet

router = DefaultRouter()
router.register("", ReportViewSet, basename="report")

urlpatterns = [
    *router.urls,
]
