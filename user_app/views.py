from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import datetime
from django.contrib import messages

from .models import *
from .forms import *


def index(request):
    categories = Category.objects.all()
    transactions = Transaction.objects.all()
    latestTransactions = Transaction.objects.filter().order_by('-id')[:3]
    locations = Location.objects.all()
    form = TransactionCreateForm()

    category_totals = calculate_category_totals()

    if request.method == 'POST':
        form = TransactionCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transaction created successfully!')

            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'categories': categories,
        'transaction': transactions,
        'latestTransactions': latestTransactions,
        'locations': locations,
        'category_totals': category_totals,
        'form': form,
    }

    return render(request, "index.html", context)


def createTransaction(request):
    return render(request, 'createTransaction.html')


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


def addCategory(request):
    categories = Category.objects.all()
    form = CategoryCreateForm()
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully!')
            return redirect(request.META.get('HTTP_REFERER'))
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, "addCategory.html", context)


def categoryTotals(request):
    category_totals = calculate_category_totals()
    context = {'category_totals': category_totals}
    return render(request, 'snippets/categoryTotals.html', context)


# Helper Functions
def calculate_category_totals():
    today = datetime.today()
    current_month = today.month
    current_year = today.year

    categories = Category.objects.all()
    category_totals = []
    for category in categories:
        total_spend = Transaction.objects.filter(
            category=category,
            date__month=current_month,
            date__year=current_year
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        category_totals.append({
            'name': category.name,
            'budget': category.budget,
            'total_spend': total_spend,
        })

    return category_totals
