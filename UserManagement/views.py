from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm


class SignupView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration/sign_up.html', {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("user registered")
            return render(request, "registration/login.html")
        else:
            return render(request, 'registration/sign_up.html', {"form": form})
