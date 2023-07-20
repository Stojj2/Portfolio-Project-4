from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BookedSlots(models.Model):
    TREATMENTS = [
    ("Cut", "Cut"),
    ("Color", "Color"),
]
    treatment = models.CharField(max_length=50, choices=TREATMENTS )
    date = models.DateTimeField(auto_now=True)
    slotID = models.CharField(max_length=5, null=False, blank=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customerID')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employeeID')

    def __str__(self):
        return f'{self.slotID}'
