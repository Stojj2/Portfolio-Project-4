from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Slot, User, Booked
from .forms import BookingForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class FreeSlots(LoginRequiredMixin, View):
    template_name = 'scheduler.html'

    def get(self, request, *args, **kwargs):
        slot = Slot.objects.all()
        booking_form = BookingForm()

        context = {
            'slot': slot,
            'booking_form': booking_form,
        }

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = BookingForm(data=request.POST)

        if form.is_valid():
            booking_instance = form.save(commit=False)
            booking_instance.customer = request.user
            booking_instance.save()

            # Update the reserved status of the chosen slot to 'True'
            slot_id = form.cleaned_data['slot'].id
            booked_slot = Slot.objects.get(pk=slot_id)
            booked_slot.reserved = True
            booked_slot.save()

            return redirect('home')
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
    template_name = 'appointments.html'

    def get(self, request, *args, **kwargs):

        booked = Booked.objects.all()
        context = {
            'booked': booked,
        }

        return render(request, self.template_name, context)


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')