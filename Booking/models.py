from django.db import models
from django.contrib.auth.models import User

#Imports for @reciever decorator 
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime


class Treatment(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Slot(models.Model):
    stylist = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    week_number = models.IntegerField(blank=True, null=True)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Slot for {self.stylist.username} on {self.date} ({self.start_time} - {self.end_time})"


@receiver(pre_save, sender=Slot)
def set_week_number(sender, instance, **kwargs):
    if instance.date:
        week_number = instance.date.isocalendar()[1]
        instance.week_number = week_number


class Booked(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking for {self.customer.username} on {self.slot.start_time} ({self.treatment.name})"

