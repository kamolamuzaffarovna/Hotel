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


class RoomBronView(View):
    template_name = 'main/index.html'

    @method_decorator(login_required, name='dispatch')
    class RoomBookingView(View):
        template_name = 'main/index.html'

        def get(self, request, *args, **kwargs):
            rid = self.kwargs.get('rid')
            path = request.GET.get('next')

            check_in = request.GET.get('check_in')
            check_out = request.GET.get('check_out')
            adults = request.GET.get('adults')
            children = request.GET.get('children')

            bron_booking = request.user.booking_set.filter(room_id=rid, booking_check_in__lt=check_out,
                                                           booking_check_out__gt=check_in).first()

            with transaction.atomic():
                if bron_booking:
                    bron_booking.delete()
                    messages.error(request, "check_out")
                else:
                    if not Booking.objects.filter(room_id=rid, booking_check_in__lt=check_out,
                                                  booking_check_out__gt=check_in).exists():
                        Booking.objects.create(
                            author=request.user,
                            room_id=rid,
                            booking_check_in=check_in,
                            booking_check_out=check_out,
                            booking_adults=adults,
                            booking_children=children
                        )
                        messages.success(request, "check_in")
                    else:
                        messages.error(request, "These rooms are already booked")
            return redirect(path)

        def post(self, request, *args, **kwargs):

            pass

        def bron_form(self, request, *args, **kwargs):
            room_choices = ["01", "02", "03", "04", "05", "06"]
            adult_choices = ["01", "02", "03", "04", "05", "06"]
            children_choices = ["01", "02", "03", "04", "05", "06"]

            if request.method == 'POST':
                form = RoomBronForm(request.POST)
                if form.is_valid():
                    check_in = form.cleaned_data['check_in']
                    check_out = form.cleaned_data['check_out']
                    room = form.cleaned_data['room']
                    adults = form.cleaned_data['adults']
                    children = form.cleaned_data['children']

                    with transaction.atomic():
                        if not Booking.objects.filter(room_id=room, booking_check_in__lt=check_out,
                                                      booking_check_out__gt=check_in).exists():
                            Booking.objects.create(
                                author=request.user,
                                room_id=room,
                                booking_check_in=check_in,
                                booking_check_out=check_out,
                                booking_adults=adults,
                                booking_children=children
                            )
                            messages.success(request, "check_in")
                        else:
                            messages.error(request, "These rooms are already booked")
                            return redirect('main:index')

            else:
                form = RoomBronForm()

            ctx = {
                'form': form,
                'room_choices': room_choices,
                'adult_choices': adult_choices,
                'children_choices': children_choices,
            }

            return render(request, self.template_name, ctx)
