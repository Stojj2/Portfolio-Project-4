from django import forms
from .models import Booked, Slot


class BookingForm(forms.ModelForm):
    """
    Form for booking a time slot and
    Setting the slot list to only show slots that is not reserved
    """

    class Meta:
        model = Booked
        fields = ('slot', 'comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slot'].queryset = Slot.objects.filter(reserved=False)


class EditForm(forms.ModelForm):
    """
    Form for editing a time slot
    """

    class Meta:
        model = Booked
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
