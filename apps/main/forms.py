from django import forms
from apps.room.models import Booking


from django import forms
from apps.room.models import Booking


class RoomBronForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'room', 'adults', 'children', 'price']

    def init(self, *args, **kwargs):
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
