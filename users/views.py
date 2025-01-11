from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import customRegistrationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    """
    Login view
    """
    template_name = 'user/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')


class SignUpView(CreateView):
    """
    Sign up view
    """
    login_url = 'login'
    template_name = 'user/register.html'
    form_class = customRegistrationForm

    def post(self, request):
        form = customRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
        else:
            return render(request, self.template_name, context={'form': form})
