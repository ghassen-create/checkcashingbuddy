from django.urls import path

from .api.viewsets import LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
]
