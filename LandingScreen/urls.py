from django.urls import path
from .views import LandingListView

urlpatterns = [
    path('landing-screen', LandingListView.as_view(), name="landing-screen"),
]
