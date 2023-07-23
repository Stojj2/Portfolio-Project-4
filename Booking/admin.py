from django.contrib import admin
from .models import Treatment, Slot, Booked

@admin.register(Booked)
class BookedAdmin(admin.ModelAdmin):

    search_fields = ['slot', 'customer', 'treatment']
    list_display = ('slot','customer', 'treatment')


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):

    search_fields = ['stylist']
    list_filter = ('stylist', 'date', 'start_time', 'end_time', 'week_number', 'reserved')
    list_display = ('stylist', 'date', 'start_time', 'end_time', 'week_number', 'reserved')

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):

    search_fields = ['name','price']
    list_display = ('name','price')