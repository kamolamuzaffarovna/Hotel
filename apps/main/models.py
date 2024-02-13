from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class DateField(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    adult = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    children = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])

    def __str__(self):
        return self.room


class Icon(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='icon/')

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField(max_length=221)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HotelContact(models.Model):
    phone = models.CharField(max_length=221, null=True, blank=True)
    address = models.CharField(max_length=221, null=True, blank=True)
    time = models.CharField(max_length=221, null=True, blank=True)
    hotel_email = models.EmailField(max_length=221, null=True, blank=True)

    def __str__(self):
        return self.phone


class Manager(models.Model):
    name = models.CharField(max_length=221)
    bio = models.TextField()

    def __str__(self):
        return self.name
