from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, View, CreateView
from .models import Room, FooterImage, Information, Service, Booking
from django.core.paginator import Paginator
from apps.main.forms import RoomBronForm


class RoomListView(ListView):
    queryset = Room.objects.all()
    paginate_by = 1

    # template_name = 'room/room_detail.html'

    def get_queryset(self):
        return Room.objects.all()

    def get_list(self):
        return Room.objects.all()

    def get_data(self):
        return Information.objects.all()

    def get_booking(self):
        return Booking.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['list'] = self.get_list()
        ctx['data'] = self.get_data()
        ctx['booking'] = self.get_booking()

        return ctx

    # def get(self, request, *args, **kwargs):
    #     form = RoomBronForm()
    #     ctx = {'form': form}
    #     return render(request, 'room/room_list.html', ctx)

    def post(self, request, *args, **kwargs):
        form = RoomBronForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if request.FILES:
                Room.objects.create(user_id=user.id, header_image=request.FILES.get('header-image'))
                messages.success(request, 'Successfully room bron')
            return redirect(reverse_lazy('room:page-detail'))


class RoomDetailView(DetailView):
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

    def get_bookings(self):
        return Booking.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['room'] = self.get_rooms()
        ctx['image'] = self.get_image()
        ctx['data'] = self.get_data()
        ctx['services'] = self.get_services()
        ctx['bookings'] = self.get_bookings()

        return ctx
