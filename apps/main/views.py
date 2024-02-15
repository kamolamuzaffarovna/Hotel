from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Icon, Manager, HotelContact, Slide
from apps.blog.models import Blog
from apps.room.models import Room


class HomeView(ListView):
    template_name = 'main/index.html'
    context_object_name = "mixed_list"

    def get_queryset(self):
        blog = Blog.objects.all()
        icon = Icon.objects.all()
        manager = Manager.objects.all()
        slide = Slide.objects.order_by()[:3]
        return list(icon) + list(manager) + list(slide) + list(blog)


class ContactView(ListView):
    queryset = HotelContact.objects.all()
    template_name = 'main/contact.html'


class AboutView(ListView):
    queryset = Manager.objects.all()
    template_name = 'main/about.html'

    context_object_name = "room_list"

    def get_queryset(self):
        room = Room.objects.all()[:3]
        manager = Manager.objects.all()
        return list(manager) + list(room)
