from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Icon, Manager, HotelContact, Slide
from apps.blog.models import Blog
from apps.room.models import Room, Information


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_blog(self):
        return Blog.objects.all()

    def get_icon(self):
        return Icon.objects.all()

    def get_manager(self):
        return Manager.objects.all()

    def get_slide(self):
        return Slide.objects.all()

    def get_room(self):
        return Room.objects.all()

    def get_information(self):
        return Information.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['blog'] = self.get_blog()
        ctx['icon'] = self.get_icon()
        ctx['manager'] = self.get_manager()
        ctx['slide'] = self.get_slide()
        ctx['room'] = self.get_room()
        ctx['data'] = self.get_information()

        return ctx


class ContactView(ListView):
    queryset = HotelContact.objects.all()
    template_name = 'main/contact.html'


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_room(self):
        return Room.objects.all()

    def get_manager(self):
        return Manager.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['rooms'] = self.get_room()
        ctx['managers'] = self.get_manager()

        return ctx
