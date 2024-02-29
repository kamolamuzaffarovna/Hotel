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
        if check_in and check_out:
            rooms = rooms.filter(
                ~Q(rooms_booking__check_in__lte=check_out) | ~Q(rooms_booking__check_out__gte=check_in))
        if adults or children:
            adults = int(adults)
            children = int(children)
            rooms = rooms.filter(Q(children=children) or Q(adults=adults))
        paginator = Paginator(rooms, 1)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

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
        ctx = {

        }
        if request.method == 'POST':
            check_in = request.POST.get('check_in')
            check_out = request.POST.get('check_out')
            if check_in is not None:
                check_in = '20' + '-'.join(check_in.split('/')[::-1])
            if check_out is not None:
                check_out = '20' + '-'.join(check_out.split('/')[::-1])
            date = {
                'check_in': check_in,
                'check_out': check_out
            }
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
            farq = abs((check_out_date - check_in_date).days)
            ctx['farq'] = farq
            form = RoomBronForm(date)
            if form.is_valid():
                if objects.is_open_for_booking and farq > 0:
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
                    messages.success(request, 'Sorry, the room is already booked!!!')
            else:
                messages.success(request, 'the room is booking!!!')

            return render(request, self.template_name, ctx)

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

    # def post(self, request, *args, **kwargs):
    #     objects = get_object_or_404(Room, slug=kwargs['slug'])
    #     form = RoomBronForm()
    #     ctx = {
    #         'objects': objects,
    #         'form': form
    #     }
    #     check_in = request.POST.get('check_in')
    #     check_out = request.POST.get('check_out')
    #     if check_in is not None:
    #         check_in = '20' + '-'.join(check_in.split('/')[::-1])
    #     if check_out is not None:
    #         check_out = '20' + '-'.join(check_out.split('/')[::-1])
    #     date = {
    #         'check_in': check_in,
    #         'check_out': check_out
    #     }
    #     check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
    #     check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
    #     farq = abs((check_out_date - check_in_date).days)
    #     ctx['farq'] = farq
    #     form = RoomBronForm(date)
    #     if form.is_valid():
    #         if objects.is_open_for_booking and farq>0:
    #             obj = form.save(commit=False)
    #             obj.objects = objects
    #             obj.author_id = request.user.id
    #             form.save()
    #             objects.is_open_for_booking = False
    #             objects.save()
    #             messages.success(request,
    #                              f'You booked the room for {farq} days and the total price ${farq * objects.price}')
    #             return redirect('.')
    #         else:
    #             messages.success(request, 'Sorry, the room is already booked!!!')
    #     else:
    #         messages.success(request, 'the room is booking!!!')
    #
    #     return render(request, self.template_name, ctx)
