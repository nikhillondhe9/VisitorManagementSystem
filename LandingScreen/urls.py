from django.urls import path
from .views import LandingView

urlpatterns = [
    path('landing-view', LandingView.as_view(), name="landing-view"),
]
