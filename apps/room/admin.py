from django.contrib import admin
from .models import (
    Room,
    Information,
    Service,
    Date,
    Guest,
    Price
)
from apps.blog.models import BaseModel


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'money', 'created_date')
    readonly_fields = ('modified_date', 'created_date')
    date_hierarchy = 'created_date'
    search_fields = ('title', )


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')
    autocomplete_fields = ('room', )
    readonly_fields = ('created_date', )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')
    autocomplete_fields = ('room', )
    readonly_fields = ('created_date', )


@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ('id', 'check_in', 'check_out', 'created_date')
    readonly_fields = ('created_date', )
    autocomplete_fields = ('room', )


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'adults', 'created_date')
    autocomplete_fields = ('room',)
    readonly_fields = ('created_date', )


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'money', 'created_date')
    autocomplete_fields = ('room',)
    readonly_fields = ('created_date', )
