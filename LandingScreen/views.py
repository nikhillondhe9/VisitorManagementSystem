from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class LandingView(LoginRequiredMixin, View):
    login_url = "/admin/"

    def get(self, request):
        return render(request, "LandingScreen/landingscreen.html")
