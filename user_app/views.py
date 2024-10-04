from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
from .forms import *


def index(request):
    catagories = Catagory.objects.all()
    transactions = Transaction.objects.filter().order_by('-id')[:3]
    locations = Location.objects.all()
    form = TransactionCreateForm()

    if request.method == 'POST':
        form = TransactionCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transaction created successfully!')

            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'catagories': catagories,
        'transactions': transactions,
        'locations': locations,
        'form': form,
    }

    return render(request, "index.html", context)


def addLocation(request):
    locations = Location.objects.all()
    form = LocationCreateForm()
    if request.method == 'POST':
        form = LocationCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Location created successfully!')
            return redirect(request.META.get('HTTP_REFERER'))
    context = {
        'locations': locations,
        'form': form,
    }
    return render(request, "addLocation.html", context)


def addCatagory(request):
    catagories = Catagory.objects.all()
    form = CatagoryCreateForm()
    if request.method == 'POST':
        form = CatagoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Catagory created successfully!')
            return redirect(request.META.get('HTTP_REFERER'))
    context = {
        'catagories': catagories,
        'form': form,
    }
    return render(request, "addCatagory.html", context)
