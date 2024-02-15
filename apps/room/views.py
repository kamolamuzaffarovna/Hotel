from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Room, FooterImage


class RoomListView(TemplateView):
    template_name = 'room/room_list.html'


class RoomDetailView(ListView):
    queryset = Room.objects.all()
    # slug_field = 'slug'
    # template_name = 'room/room_detail.html'

