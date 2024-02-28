from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView
from .models import Icon, Manager, HotelContact, Slide, Contact
from apps.blog.models import Blog
from apps.room.models import Room, Information, Booking
from .forms import RoomBronForm
from apps.room.forms import ContactForm
from django.urls import reverse_lazy


class HomeView(View):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.all()[:3]
        icon = Icon.objects.all()
        manager = Manager.objects.all()
        slide = Slide.objects.all()
        rooms = Room.objects.all()
        data = Information.objects.all()
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        adults = request.GET.get('adults')
        children = request.GET.get('children')
        if check_in and check_out:
            rooms = rooms.filter(~Q(booking__check_in__lte=check_out) | ~Q(booking__check_out__gte=check_in))
        if adults or children:
            adults = int(adults)
            children = int(children)
            rooms = rooms.filter(Q(children=children) or Q(adults=adults))

        ctx = {
            'blog': blog,
            'icon': icon,
            'manager': manager,
            'slide': slide,
            'rooms': rooms,
            'data': data,
        }

        return render(request, self.template_name, ctx)


class ContactView(CreateView):
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('main:contact')


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_room(self):
        return Room.objects.all()[:3]

    def get_manager(self):
        return Manager.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['rooms'] = self.get_room()
        ctx['managers'] = self.get_manager()

        return ctx
