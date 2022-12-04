from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from RequestScreen.models import VisitRequestDetails
# from .models import VisitRequestDetail


# Create your views here.


class LandingListView(LoginRequiredMixin, ListView):
    login_url = "/login"
    model = VisitRequestDetails
    template_name = 'LandingScreen/VisitRequestDetails_list.html'
    paginate_by = 10
    context_object_name = "visit_requests"
