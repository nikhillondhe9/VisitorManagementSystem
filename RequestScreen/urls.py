from django.urls import path
from .views import RequestScreenView

urlpatterns = [
    path('request-screen', RequestScreenView.as_view(), name="request-screen")
]
