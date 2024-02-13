from django.contrib import admin
from .models import (
    DateField,
    Icon,
    Contact,
    HotelContact,
    Manager
)


@admin.register(DateField)
class DateFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'check_in', 'check_out', 'room')
    search_fields = ('room', )


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_date')
    readonly_fields = ('created_date', )
    search_fields = ('name', )


@admin.register(HotelContact)
class HotelContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address', 'hotel_email')


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )