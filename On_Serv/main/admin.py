from django.contrib import admin

# Register your models here.
from .models import Make, V_model, Service_Interval, Vehicle, Company, Service

# Register your models here.
admin.site.register(Make)
admin.site.register(V_model)
admin.site.register(Service_Interval)
admin.site.register(Vehicle)
admin.site.register(Company)
admin.site.register(Service)