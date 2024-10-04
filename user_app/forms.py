from django.forms import ModelForm
from django import forms
from .models import *


class TransactionCreateForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'location', 'amount', 'catagory']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class LocationCreateForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name']


class CatagoryCreateForm(ModelForm):
    class Meta:
        model = Catagory
        fields = ['name', 'budget']
