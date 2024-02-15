from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Room, FooterImage, Information, Service


class RoomListView(TemplateView):
    template_name = 'room/room_list.html'


class RoomDetailView(TemplateView):
    template_name = 'room/room_detail.html'

    def get_rooms(self):
        return Room.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['room'] = self.get_rooms()
        ctx['image'] = FooterImage.objects.all()
        ctx['information'] = Information.objects.all()
        ctx['services'] = Service.objects.all()

        return ctx

