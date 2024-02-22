from django import forms
from apps.room.models import Booking


class RoomBronForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'room', 'adults', 'children', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['check_in'].widget.attrs.update({
            'type': 'text',
            'class': 'input-small form-control',
            'id': 'checkInDate',
            'name': 'checkInDate',
            'placeholder': 'Check In'
        })
        self.fields['check_out'].widget.attrs.update({
            'type': 'text',
            'class': 'input-small form-control',
            'name': 'checkOutDate',
            'placeholder': 'Check Out'
        })
        self.fields['adults'].widget.attrs.update({
            'class': 'form-control',
            'id': 'guests',
            'name': 'adults',
        })
        self.fields['room'].widget.attrs.update({
            'class': 'input-small form-control',
            'id': 'checkInDate',
            'name': 'checkInDate',
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

