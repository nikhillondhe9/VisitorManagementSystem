from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate


class SignupView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration/sign_up.html', {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("user registered")
            return redirect('/request-screen')

        else:
            form = RegistrationForm()

        return render(request, 'registration/sign_up.html', {"form": form})
