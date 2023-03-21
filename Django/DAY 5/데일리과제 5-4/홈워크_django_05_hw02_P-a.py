from django import forms
from .models import Reservation

# class ReservationForm(__(a)__):

#     class __(b)__:
#         model = Reservation
#         fields = '__all__'

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = '__all__'