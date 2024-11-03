from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import datetime
from datetime import date
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


def viewTransactions(request):
    transactions = Transaction.objects.filter(location__name="Bank of America")

    context = {
        'transactions': transactions,
    }
    return render(request, "viewTransactions.html", context)


def viewMonth(request):
    form = MonthSelectForm(request.POST or None)
    transactions = None
    selected_month = None
    month_name = None

    if request.method == 'POST' and form.is_valid():
        selected_month = int(form.cleaned_data['month'])
        transactions = Transaction.objects.filter(
            date__month=selected_month).order_by('date')
        month_name = MONTH_NAMES.get(selected_month)
        category_totals = monthly_category_totals(selected_month)

    context = {
        'form': form,
        'transactions': transactions,
        'selected_month': selected_month,
        'month_name': month_name,
        'category_totals': category_totals
    }
    return render(request, "viewMonth.html", context)


def updateTransaction(request, id):
    transaction = Transaction.objects.get(id=id)
    form = TransactionCreateForm(instance=transaction)

    context = {
        'transaction': transaction,
        'form': form,
    }
    return render(request, "updateTransaction.html", context)

# Snippets


def createTransaction(request):
    return render(request, 'createTransaction.html')


def latestTransactions(request):
    return render(request, 'snippets/latestTransactions.html')


def categoryTotals(request):
    category_totals = calculate_category_totals()
    context = {'category_totals': category_totals}
    return render(request, 'snippets/categoryTotals.html', context)

# Helper Functions


MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}


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


def monthly_category_totals(month):
    month = month

    categories = Category.objects.all()
    category_totals = []
    for category in categories:
        total_spend = Transaction.objects.filter(
            category=category,
            date__month=month,
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        category_totals.append({
            'name': category.name,
            'budget': category.budget,
            'total_spend': total_spend,
        })

    return category_totals
