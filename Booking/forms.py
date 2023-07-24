from django import forms
from .models import Booked, Slot

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booked
        fields = ('slot', 'comment',)
        widgets = {
            #'slot': forms.RadioSelect(attrs={'class': 'slot-radio'}),
            'comment': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slot'].queryset = Slot.objects.filter(reserved=False)
