from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Vehicle, Company, Service
from .forms import add_vehicle_form, add_company_form, add_service_form
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# About Us page
@login_required()
def about(request):
    return render(request, "about.html")

@login_required()
def list_vehicles(request):
    vehicle_list = Vehicle.objects.all()
    return render(request, "vehicles.html", {'vehicle_list': vehicle_list })

@login_required()
def add_vehicle(request):
    submitted = False

    if request.method == "POST":
        form = add_vehicle_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:list_vehicles')
    else:
        form = add_vehicle_form()

    if 'submitted' in request.GET:
        submitted = True

    return render(request, "add_vehicle.html", {"form": form, 'submitted': submitted})

@login_required()
def list_companies(request):
    company_list = Company.objects.all()
    return render(request, "companies.html",{"company_list": company_list} )

@login_required()
def add_company(request):
    submitted = False

    if request.method == "POST":
        form = add_company_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:list_companies')
    else:
        form = add_company_form()
    
    if 'submitted' in request.GET:
        submitted = True

    return render(request, "add_company.html", {"form": form, 'submitted': submitted})

@login_required()
def list_services(request):
    service_list = Service.objects.all()
    return render(request, "services.html", {"service_list": service_list})

@login_required()
def add_service(request):
    submitted = False

    if request.method == "POST":
        form = add_service_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:list_services')
    else:
        form = add_service_form()
    
    if 'submitted' in request.GET:
        submitted = True

    return render(request, "add_service.html", {"form": form, 'submitted': submitted})

