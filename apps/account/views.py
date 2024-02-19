from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import auth_logout
from django.contrib import messages
from .models import ContactPicture
from .forms import RegisterForm


class LoginView(TemplateView):
    template_name = 'account/login.html'


class LogoutView(View):
    template_name = 'account/logout.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        auth_logout(request)
        messages.success(request, "Successfully logged out")
        return redirect('/')


class RegisterView(View):
    template_name = 'account/register.html'

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if request.FILES:
                ContactPicture.objects.create(user_id=user.id, picture=request.FILES.get('image'))
                messages.success(request, "Successfully registered")
            return redirect(reverse_lazy('account:login'))