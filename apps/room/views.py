from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Room, FooterImage, Information, Service, Booking
from django.core.paginator import Paginator
from apps.main.forms import RoomBronForm


class RoomListView(View):
    template_name = 'room/room_list.html'

    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        data = Information.objects.all()
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        adults = request.GET.get('adults')
        children = request.GET.get('children')
        paginator = Paginator(rooms, 1)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        if check_in and check_out:
            rooms = rooms.filter(~Q(booking__check_in__lte=check_out) | ~Q(booking__check_out__gte=check_in))
        if adults or children:
            adults = int(adults)
            children = int(children)
            rooms = rooms.filter(Q(children=children) or Q(adults=adults))

        ctx = {
            'rooms': rooms,
            'data': data,
            'page_obj': page_obj
        }

        return render(request, self.template_name, ctx)


class RoomDetailView(View):
    template_name = 'room/room_detail.html'

    def get(self, request, *args, **kwargs):
        objects = get_object_or_404(Room, slug=kwargs['slug'])
        form = RoomBronForm()
        image = FooterImage.objects.all()
        data = Information.objects.all()
        services = Service.objects.all()
        bookings = Booking.objects.all()
        rooms = Room.objects.all()
        ctx = {
            'objects': objects,
            'image': image,
            'data': data,
            'services': services,
            'bookings': bookings,
            'rooms': rooms,
            'form': form
        }

        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        objects = get_object_or_404(Room, slug=kwargs['slug'])
        form = RoomBronForm()
        ctx = {
            'objects': objects,
            'form': form
        }
        check_in = '20' + '-'.join(request.POST['check_in'].split('/')[::-1])
        check_out = '20' + '-'.join(request.POST['check_out'].split('/')[::-1])
        date = {
            'check_in': check_in,
            'check_out': check_out,
        }
        print(check_in, check_out)
        farq = abs((datetime.strptime(check_out, '%Y-%m-%d') - datetime.strptime(check_in, '%Y-%m-%d')).days)
        ctx['farq'] = farq
        form = RoomBronForm(date)
        print(form.errors)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.objects = objects
            obj.author_id = request.user.id
            form.save()
            objects.is_open_for_booking = False
            objects.save()
            messages.success(request,
                             f'You booked the room for {farq} days and the total price ${farq * objects.price}')
            return redirect('.')
        else:
            messages.success(request, 'the room is booking!!!')

        return render(request, self.template_name, ctx)
