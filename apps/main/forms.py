from django import forms
from apps.room.models import Booking


class RoomBronForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'room', 'adults', 'children']
