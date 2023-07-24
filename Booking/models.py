from django.db import models
from django.contrib.auth.models import User

#Imports for @reciever decorator 
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime


class Slot(models.Model):
    stylist = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    reserved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Slot for {self.stylist.username} on {self.date} ({self.start_time} - {self.end_time})"


class Booked(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Booking for {self.customer.username} on {self.slot.start_time}"

