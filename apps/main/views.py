from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Icon, Manager, HotelContact


class HomeView(ListView):
    template_name = 'main/index.html'
    context_object_name = "mixed_list"

    def get_queryset(self):
        icon = Icon.objects.all()
        manager = Manager.objects.all()
        return list(icon) + list(manager)


class ContactView(ListView):
    queryset = HotelContact.objects.all()
    template_name = 'main/contact.html'


class AboutView(TemplateView):
    template_name = 'main/about.html'
