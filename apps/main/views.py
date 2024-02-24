from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView
from .models import Icon, Manager, HotelContact, Slide, Contact
from apps.blog.models import Blog
from apps.room.models import Room, Information, Booking
from .forms import RoomBronForm
from apps.room.forms import ContactForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_blog(self):
        return Blog.objects.all()[:3]

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

    def get(self, request, *args, **kwargs):
        rid = self.kwargs.get('rid')
        # path = request.GET.get('next')

        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        adults = request.GET.get('adults')
        children = request.GET.get('children')
        # if rid is not None and check_in is not None and check_out is not None:
        if request.user.booking_set.filter(room_id=rid, check_in__lte=check_out,
                                           check_out__gte=check_in).exists():
            request.user.booking_set.filter(room_id=rid, check_in__lte=check_out,
                                            check_out__gte=check_in).delete()
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

        return redirect('.')
    # else:


#     messages.error(request, "Invalid parameters provided.")
#     return redirect(reverse_lazy('main:home'))

def post(self, request, *args, **kwargs):
    form = RoomBronForm(data=request.POST)
    if form.is_valid():
        booking = form.save(commit=False)
        booking.author = request.user
        booking.save()
        if request.FILES:
            Room.objects.create(user=request.user, header_image=request.FILES.get('header-image'))
            messages.success(request, "Successfully room bron")
            return redirect(reverse_lazy('room:page-detail'))


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
