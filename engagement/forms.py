from django import forms
from .models import VolunteerApplication


class VolunteerForm(forms.ModelForm):

    class Meta:
        model = VolunteerApplication

        fields = [
            'name',
            'email',
            'phone',
            'skills',
            'campaign'
        ]
        
from .models import Donation


class DonationForm(forms.ModelForm):

    class Meta:

        model = Donation

        fields = [
            'name',
            'email',
            'campaign',
            'amount'
        ]