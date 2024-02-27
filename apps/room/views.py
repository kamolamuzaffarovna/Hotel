from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, View, CreateView
from .models import Room, FooterImage, Information, Service, Booking
from django.core.paginator import Paginator
from apps.main.forms import RoomBronForm


class RoomListView(View):
    template_name = 'room/room_list.html'

    def get(self, request, *args, **kwargs):
        rooms = Room.objects.order_by('-id')
        data = Information.objects.all()
        booking = Booking.objects.all()
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        adults = request.GET.get('adults')
        children = request.GET.get('children')
        if check_in and check_out:
            rooms = rooms.filter(~Q(booking__check_in__lte=check_out) | ~Q(booking__check_out__gte=check_in))
        if adults or children:
            if type(adults) == str:
                adults = 0
            if type(children) == str:
                children = 0
            adults = int(adults)
            children = int(children)
            rooms = rooms.filter(Q(children__gte=children) or Q(adults__gte=adults))
        paginator = Paginator(rooms, 1)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        ctx = {
            'rooms': rooms,
            'data': data,
            'page_obj': page_obj
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = RoomBronForm(data=request.POST)
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        adults = request.POST.get('adults', 0)
        children = request.POST.get('children', 0)

        if form.is_valid():
            form.save()
        else:
            Booking.objects.create(check_in=check_in, check_out=check_out, adults=adults, children=children)
            messages.success(request, 'Check-in successful')

        ctx = {
            'check_in': check_in,
            'check_out': check_out,
            'adults': adults,
            'children': children
        }

        return render(request, self.template_name, ctx)




# def get(self, request, *args, **kwargs):
#     # rid = self.kwargs.get('rid')
#     path = request.GET.get('next')
#     rid = request.GET.get('rid')
#     check_in = request.GET.get('check_in')
#     check_out = request.GET.get('check_out')
#     adults = request.GET.get('adults')
#     children = request.GET.get('children')
#
#     if rid and check_in and check_out:
#
#         adults = adults or 0
#
#         children = children or 0
#
#         if request.user.booking_set.filter(room_id=rid, check_in__lt=check_out, check_out__gt=check_in).exists():
#             request.user.booking_set.filter(room_id=rid, check_in__lt=check_out, check_out__gt=check_in).delete()
#             messages.success(request, "These rooms are already booked")
#
#         else:
#             Booking.objects.create(
#                 author=request.user,
#                 room_id=rid,
#                 check_in=check_in,
#                 check_out=check_out,
#                 adults=adults,
#                 children=children
#             )
#             messages.success(request, "check_in")
#     else:
#         messages.error(request, "Missing or invalid parameters for booking")
#
#     return redirect('.')
#
# def post(self, request, *args, **kwargs):
#     form = RoomBronForm(data=request.POST)
#     if form.is_valid():
#         user = form.save()
#         if request.FILES:
#             Room.objects.create(user_id=user.id, header_image=request.FILES.get('header-image'))
#             messages.success(request, 'Successfully room bron')
#         return redirect(reverse_lazy('room:page-list'))
#     else:
#         messages.error(request, 'Form is not valid. Please check your inputs.')
#         ctx = self.get_context_data()
#         ctx['form'] = form
#         return render(request, self.template_name, ctx)


class RoomDetailView(View):
    template_name = 'room/room_detail.html'

    def get(self, request, *args, **kwargs):
        objects = get_object_or_404(Room, slug=kwargs['slug'])
        image = FooterImage.objects.all()
        data = Information.objects.all()
        services = Service.objects.all()
        bookings = Booking.objects.all()
        ctx = {
            'objects': objects,
            'image': image,
            'data': data,
            'services': services,
            'bookings': bookings,
        }

        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = RoomBronForm(request.POST)
        objects = get_object_or_404(Room, slug=kwargs['slug'])
        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            adults = form.cleaned_data['adults']
            children = form.cleaned_data['children']

            Booking.objects.create(
                check_in=check_in,
                adults=adults,
                children=children,
                check_out=check_out,
            )
            messages.success(request, 'Successfully room bron')
        else:
            check_in = request.POST.get('check_in')
            check_out = request.POST.get('check_out')
            adults = request.POST.get('adults')
            children = request.POST.get('children')

        if not adults or not adults.isdigit():
            adults = 0
        if not children or not children.isdigit():
            children = 0

        adults = int(adults)
        children = int(children)

        ctx = {
            'check_in': check_in,
            'check_out': check_out,
            'adults': adults,
            'children': children,
            'form': form,
            'image': FooterImage.objects.all(),
            'data': Information.objects.all(),
            'services': Service.objects.all(),
            'bookings': Booking.objects.all(),
            'objects': objects
        }
        return render(request, self.template_name, ctx)
