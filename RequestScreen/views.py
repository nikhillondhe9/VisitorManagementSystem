from django.shortcuts import render
from django.views import View

# Create your views here.


class RequestScreenView(View):
    def get(self, request):
        return render(request, "RequestScreen/request_screen.html")
