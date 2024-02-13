from django.shortcuts import render
from django.views.generic import TemplateView


class RoomListView(TemplateView):
    template_name = 'room/room_list.html'


class RoomDetailView(TemplateView):
    template_name = 'room/room_detail.html'
