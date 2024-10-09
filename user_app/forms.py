from django.forms import ModelForm
from django import forms
from .models import *


class TransactionCreateForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'location', 'amount', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form'}),
            'location': forms.Select(attrs={'class': 'form'}),
            'category': forms.Select(attrs={'class': 'form'}),
        }

    amount = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form'}),
        max_digits=10,
        decimal_places=2
    )


class LocationCreateForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name']


class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'budget']
