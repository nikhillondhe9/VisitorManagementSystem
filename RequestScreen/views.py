from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import VisitRequestDetails
from .forms import VisitRequestDetailsForm


# Create your views here.
class RequestScreenView(LoginRequiredMixin, View):

    login_url = "/login"

    def get(self, request):
        form = VisitRequestDetailsForm()
        return render(request, "RequestScreen/request_screen.html", {"form": form})

    def post(self, request):
        form = VisitRequestDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "RequestScreen/request_screen.html", {"form": form})
        else:
            form = VisitRequestDetailsForm()
            return render(request, "RequestScreen/request_screen.html", {"form": form})
