from django.shortcuts import render
from django.views.generic import TemplateView, View


class LoginView(TemplateView):
    template_name = 'account/login.html'


class LogoutView(TemplateView):
    template_name = 'account/logout.html'


class RegisterView(TemplateView):
    template_name = 'account/register.html'
