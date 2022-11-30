from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class RequestScreenView(LoginRequiredMixin, View):

    login_url = "/login"

    def get(self, request):
        return render(request, "RequestScreen/request_screen.html")
