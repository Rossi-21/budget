from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add/Location/', views.addLocation, name='add-location'),
    path('add/Catagory/', views.addCatagory, name='add-catagory'),
]
