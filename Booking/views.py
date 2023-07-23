from django.shortcuts import render
from django.views import generic, View
from .models import Slot, User, Booked, Treatment



class FreeSlots(View):
    template_name = 'scheduler.html'

    def get(self, request, *args, **kwargs):

        slot = Slot.objects.all()
        stylist = User.objects.filter(is_staff=True)
        treatment = Treatment.objects.all()
        context = {
            'slot': slot,
            'stylist': stylist,
            'treatment': treatment,
        }

        return render(request, self.template_name, context)



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def scheduler(request):


    return render(request, 'scheduler.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')