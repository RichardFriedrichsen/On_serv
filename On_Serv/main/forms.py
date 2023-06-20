from django import forms
from django.forms import ModelForm
from .models import Vehicle, Company, Service

class add_vehicle_form(ModelForm):
    class Meta: 
        model = Vehicle
        fields =('vehicle_make','v_model','vin_no','engine_no','service_intervall','last_service','current_milage')

class add_company_form(ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'phone', 'email', 'address', 'postal', 'area')

class add_service_form(ModelForm):
    class Meta:
        model = Service
        fields = ('company', 'serviced_vehicle', 'service_date', 'service_type', 'serviced_at', 'cost')
