from django import forms
from apps.main.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'type': 'text',
            'name': 'message-name',
            'class': 'form-control mb-30',
            'placeholder': 'Your Name'
        })
        self.fields['email'].widget.attrs.update({
            'type': 'email',
            'name': 'message-email',
            'class': 'form-control mb-30',
            'placeholder': 'Your Email'
        })
        self.fields['name'].widget.attrs.update({
            'name': 'message',
            'class': 'form-control mb-30',
            'placeholder': 'Your Message'
        })
