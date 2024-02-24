from django import forms
from apps.room.models import Booking


class RoomBronForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'room', 'adults', 'children', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['check_in'].widget.attrs.update({
            'type': 'date',
            'class': 'form-control',
            'id': 'checkIn',
            'name': 'check_in',
            'placeholder': 'Check In'
        })
        self.fields['check_out'].widget.attrs.update({
            'type': 'date',
            'class': 'form-control',
            'id': 'checkOut',
            'name': 'check_out',
            'placeholder': 'Check Out'
        })
        self.fields['adults'].widget.attrs.update({
            'class': 'form-control',
            'id': 'adults',
            'name': 'adults',
        })
        self.fields['room'].widget.attrs.update({
            'class': 'form-control',
            'id': 'room',
            'name': 'room',
        })
        self.fields['children'].widget.attrs.update({
            'class': 'form-control',
            'id': 'children',
            'name': 'children',
        })
        # self.fields['price'].widget.attrs.update({
        #     'type': 'text',
        #     'class': 'input-small form-control',
        #     'id': 'checkInDate',
        #     'name': 'checkInDate',
        #     'placeholder': 'Check In'
        # })

