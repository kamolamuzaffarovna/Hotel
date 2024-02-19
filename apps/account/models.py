from django.db import models
from django.contrib.auth.models import User


class ContactPicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    picture = models.ImageField(upload_to='accounts/')

    def __str__(self):
        return f"{self.user.username}'s photo"
