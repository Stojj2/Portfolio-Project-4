from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Slot, User, Booked
from .forms import BookingForm, EditForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class FreeSlots(LoginRequiredMixin, View):
    template_name = 'Booking/scheduler.html'

    def get(self, request, *args, **kwargs):
        # Get booking information from database and renders the scheduler.html page
        slot = Slot.objects.all()
        booking_form = BookingForm()

        context = {
            'slot': slot,
            'booking_form': booking_form,
        }

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        # Posting booking information to database and renders the appointments.html page
        form = BookingForm(data=request.POST)

        if form.is_valid():
            booking_instance = form.save(commit=False)
            booking_instance.customer = request.user
            dubblebooked = Booked.objects.filter(customer=request.user, slot__date=booking_instance.slot.date).exists()

            if dubblebooked:
                messages.error(request, "you already have a booked slot on this date")
                return redirect('FreeSlots')

            booking_instance.save()

            # Update the reserved status of the chosen slot to 'True'
            slot_id = form.cleaned_data['slot'].id
            booked_slot = Slot.objects.get(pk=slot_id)
            booked_slot.reserved = True
            booked_slot.save()

            return redirect('appointments')
        else:
            slots = Slot.objects.all()
            stylist = User.objects.filter(is_staff=True)
            booking_form = BookingForm()

            context = {
                'slot': slot,
                'booking_form': booking_form
            }

            return render(request, self.template_name, context)


class Appointments(LoginRequiredMixin, View):
    template_name = 'Booking/appointments.html'

    def get(self, request, *args, **kwargs):
        # Get booking information from database and renders the appointments.html page
        booked = Booked.objects.all()

        # Checking if logged in user has any booked appointments
        user_booked_slots = Booked.objects.filter(customer=request.user)
        has_booked_slots = user_booked_slots.exists()

        context = {
            'booked': booked,
            'has_booked_slots': has_booked_slots,
        }

        return render(request, self.template_name, context)


def edit_appointments(request, item_id):
    # Edit the item from the database, renders the edit_appointments.html page
    item = get_object_or_404(Booked, id=item_id)
    if request.method == 'POST':
        edit_form = EditForm(request.POST, instance=item)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('appointments')

    edit_form = EditForm(instance=item)
    context = {
        'edit_form': edit_form,
    }
    return render(request, 'Booking/edit_appointments.html', context)


def delete_appointments(request, item_id):
    # Delete the item from the database and setting the slot reserved status to False
    item = get_object_or_404(Booked, id=item_id)
    slot_instance = item.slot
    slot_instance.reserved = False
    slot_instance.save()
    item.delete()
    return redirect('appointments')


def home(request):
    return render(request, 'Booking/home.html')


def about(request):
    return render(request, 'Booking/about.html')
