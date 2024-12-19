from django.forms import forms

from .models import Congratulation
# from birthday.models import Birthday


class CongratulationForm(forms.ModelForm):
    
    class Meta:
        model = Congratulation
        fields = ('text',) 