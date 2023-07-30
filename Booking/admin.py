from django.contrib import admin
from .models import Slot, Booked


@admin.register(Booked)
class BookedAdmin(admin.ModelAdmin):
    """
    Chaning admin page for the Booked table
    """

    search_fields = ['slot', 'customer', 'treatment']
    list_display = ('slot', 'customer', 'comment')


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    """
    Chaning admin page for the Slot table
    """

    search_fields = ['stylist']
    list_filter = ('stylist', 'date', 'start_time', 'end_time', 'reserved')
    list_display = ('stylist', 'date', 'start_time', 'end_time', 'reserved')
