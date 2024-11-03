from django.forms import ModelForm
from django import forms
from .models import *


class TransactionCreateForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'location', 'amount', 'category', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form'}),
            'location': forms.Select(attrs={'class': 'form'}),
            'category': forms.Select(attrs={'class': 'form'}),
            'note': forms.Textarea(attrs={'class': 'form'}),
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


class MonthSelectForm(forms.Form):
    month = forms.ChoiceField(
        choices=[(str(i), month) for i, month in enumerate(
            ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], 1)],
        label='Select Month',
        widget=forms.Select(attrs={'class': 'form'})
    )

# Todo


class TransactionFilterForm(forms.Form):
    location = forms.ModelChoiceField(queryset=Location.objects.all(
    ), required=False, label='Location', empty_label='Select Location')
    category = forms.ModelChoiceField(queryset=Category.objects.all(
    ), required=False, label='Category', empty_label='Select Category')
    date_start = forms.DateField(required=False, label='Start Date', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form'}))
    date_end = forms.DateField(required=False, label='End Date', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget.attrs.update({'class': 'form'})
        self.fields['category'].widget.attrs.update({'class': 'form'})
