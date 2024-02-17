from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Room, FooterImage, Information, Service
from django.core.paginator import Paginator


class RoomListView(ListView):
    model = Room
    template_name = 'room/room_list.html'
    paginate_by = 1

    def get_queryset(self):
        return Room.objects.all()

    def get_list(self):
        return Room.objects.all()

    def get_data(self):
        return Information.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['list'] = self.get_list()
        ctx['data'] = self.get_data()

        return ctx


class RoomDetailView(DetailView):
    template_name = 'room/room_detail.html'
    queryset = Room.objects.all()
    slug_field = 'slug'

    def get_rooms(self):
        return Room.objects.all()

    def get_image(self):
        return FooterImage.objects.all()

    def get_data(self):
        return Information.objects.all()

    def get_services(self):
        return Service.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['room'] = self.get_rooms()
        ctx['image'] = self.get_image()
        ctx['data'] = self.get_data()
        ctx['services'] = self.get_services()

        return ctx

