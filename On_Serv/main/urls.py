from django.contrib import admin
from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.about, name="index"),
    path('list_vehicles/', views.list_vehicles, name="list_vehicles"),
    path('add_vehicle/', views.add_vehicle , name="add_vehicle"),
    path('list_companies/', views.list_companies , name="list_companies"),
    path('add_company/', views.add_company , name="add_company"),
    path('list_services/', views.list_services , name="list_services"),
    path('add_service/', views.add_service , name="add_service"),
    
]

