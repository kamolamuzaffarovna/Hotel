# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
#
# class CommentForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'message']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs.update({
#             'type': 'text',
#             'name': 'message-name',
#             'class': 'form-control mb-30',
#             'placeholder': 'Your Name'
#         })
#         self.fields['email'].widget.attrs.update({
#             'type': 'email',
#             'name': 'message-email',
#             'class': 'form-control mb-30',
#             'placeholder': 'Your Email'
#         })
#         self.fields['message'].widget.attrs.update({
#             'name': 'message',
#             'class': 'form-control mb-30',
#             'placeholder': 'Start the discussion...'
#         })