from django import forms
from . models import Whiskey


class CreateWhiskeyForm(forms.ModelForm):
    class Meta:
        model = Whiskey
        fields = ['name', 'price','mocnist','description']