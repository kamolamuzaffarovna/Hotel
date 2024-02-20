from django.db import models
from apps.blog.models import BaseModel
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

from utils.make_slug import make_slugify


class Room(BaseModel):
    title = models.CharField(max_length=221)
    money = models.CharField(max_length=221)
    slug = models.SlugField(max_length=221, null=True, blank=True)
    header_image = models.ImageField(upload_to='room/')
    content = RichTextField()

    def __str__(self):
        return self.title


class FooterImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='room/footer_image/')


class Information(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='data')
    title = models.CharField(max_length=221)
    footer_title = models.CharField(max_length=221, null=True, blank=True)

    def __str__(self):
        return self.title


class Service(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='services')
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='room/service')

    def __str__(self):
        return self.title


class Booking(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='booking')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.check_in}'

    # class Meta:
    #     unique_together = ('room', 'check_in', 'check_out')
    #
    # def save(self, *args, **kwargs):
    #     if not self.pk and Booking.objects.filter(
    #         room=self.room,
    #         check_in__lt=self.check_out,
    #         check_out__gt=self.check_in,
    #     ).exists():
    #
    #         raise ValueError("These rooms are already booked")
    #     super().save(*args, **kwargs)


@receiver(pre_save, sender=Room)
def room_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        make_slugify(instance)
