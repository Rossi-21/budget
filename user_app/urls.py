from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add/location/', views.addLocation, name='add-location'),
    path('add/category/', views.addCategory, name='add-category'),
    path('create/transaction', views.createTransaction, name='create-transaction'),
    path('categoryTotals/', views.categoryTotals, name='category-totals'),
]
