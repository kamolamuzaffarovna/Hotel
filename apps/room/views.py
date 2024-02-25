from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, View, CreateView
from .models import Room, FooterImage, Information, Service, Booking
from django.core.paginator import Paginator
from apps.main.forms import RoomBronForm
from .. import room


class RoomListView(ListView):
    queryset = Room.objects.all()
    # model = Room
    # template_name = 'room/room_list.html'
    # context_object_name = 'object_list'
    paginate_by = 1

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
        # ctx['form'] = RoomBronForm()
        return ctx

    def get(self, request, *args, **kwargs):
        # rid = self.kwargs.get('rid')
        # path = request.GET.get('next')

        rid = request.GET.get('rid')
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        adults = request.GET.get('adults')
        children = request.GET.get('children')

        if rid and check_in and check_out:

            adults = adults or 0

            children = children or 0

            if request.user.booking_set.filter(room_id=rid, check_in__lt=check_out, check_out__gt=check_in).exists():
                request.user.booking_set.filter(room_id=rid, check_in__lt=check_out, check_out__gt=check_in).delete()
                messages.success(request, "These rooms are already booked")

            else:
                Booking.objects.create(
                    author=request.user,
                    room_id=rid,
                    check_in=check_in,
                    check_out=check_out,
                    adults=adults,
                    children=children
                )
                messages.success(request, "check_in")
        else:
            messages.error(request, "Missing or invalid parameters for booking")

        return redirect('.')

    def post(self, request, *args, **kwargs):
        form = RoomBronForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if request.FILES:
                Room.objects.create(user_id=user.id, header_image=request.FILES.get('header-image'))
                messages.success(request, 'Successfully room bron')
            return redirect(reverse_lazy('room:page-list'))
        else:
            messages.error(request, 'Form is not valid. Please check your inputs.')
            ctx = self.get_context_data()
            ctx['form'] = form
            return render(request, self.template_name, ctx)


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
