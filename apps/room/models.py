from django.db import models
from apps.blog.models import BaseModel
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator


class Room(BaseModel):
    title = models.CharField(max_length=221)
    money = models.CharField(max_length=221)
    header_image = models.ImageField(upload_to='room/')
    footer_image = models.ImageField(upload_to='room/')
    content = RichTextField()

    def __str__(self):
        return self.title


class Information(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='data')
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='room/information/')

    def __str__(self):
        return self.title


class Service(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='services')
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='room/service')

    def __str__(self):
        return self.title


class Date(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='dates')
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return self.check_in


class Guest(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='guests')
    adults = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    children = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])

    def __str__(self):
        return self.adults


class Price(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='prices')
    money = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3000)])

    def __str__(self):
        return self.money
