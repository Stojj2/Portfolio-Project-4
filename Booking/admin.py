from django.contrib import admin
from .models import Slot, Booked


@admin.register(Booked)
class BookedAdmin(admin.ModelAdmin):

    search_fields = ['slot', 'customer', 'treatment']
    list_display = ('slot', 'customer', 'comment')


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):

    search_fields = ['stylist']
    list_filter = ('stylist', 'date', 'start_time', 'end_time', 'reserved')
    list_display = ('stylist', 'date', 'start_time', 'end_time', 'reserved')
