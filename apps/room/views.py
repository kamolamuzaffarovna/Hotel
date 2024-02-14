from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Room, FooterImage


class RoomListView(TemplateView):
    template_name = 'room/room_list.html'


class RoomDetailView(DetailView):
    queryset = Room.objects.all()
    slug_field = 'slug'
    template_name = 'room/room_detail.html'

    def get_footer_image(self):
        return FooterImage.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['footer_image'] = self.get_footer_image()

        return ctx
