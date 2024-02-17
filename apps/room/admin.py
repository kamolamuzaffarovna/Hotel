from django.contrib import admin
from .models import (
    Room,
    Information,
    Service,
    Booking,
    FooterImage
)
from apps.blog.models import BaseModel


class FooterImageInline(admin.StackedInline):
    model = FooterImage
    extra = 0


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'money', 'created_date')
    readonly_fields = ('modified_date', 'created_date')
    date_hierarchy = 'created_date'
    search_fields = ('title', )
    inlines = [FooterImageInline]


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


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'check_in', 'check_out', 'created_date')
    readonly_fields = ('created_date', )
    autocomplete_fields = ('room', )