from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add/location/', views.addLocation, name='add-location'),
    path('add/category/', views.addCategory, name='add-category'),
    path('transactions/', views.viewTransactions, name="view-transactions"),
    path('transactions/update/<int:id>',
         views.updateTransaction, name="update-transaction"),
    path('view/month', views.viewMonth, name="view-month"),

    # snippets
    path('create/transaction', views.createTransaction,
         name='create-transaction'),
    path('categoryTotals/', views.categoryTotals, name='category-totals'),
    path('latestTransactions/', views.latestTransactions,
         name="latest-transactions")
]
