from django.db import models

# Create your models here.

class Make(models.Model):
    vehicle_make = models.CharField(max_length=100)
    
    def __str__(self):
        return self.vehicle_make


class V_model(models.Model):
    vehicle_make = models.ForeignKey(Make, on_delete=models.CASCADE)
    v_model = models.CharField(max_length=100)

    def __str__(self):
        return self.v_model
    
class Service_Interval(models.Model):
    service_intervall = models.IntegerField()

    def __str__(self):
        return str(self.service_intervall)


# 'vehicle_make','v_model','vin_no','engine_no','service_intervall','last_service','current_milage'
class Vehicle(models.Model):
    vehicle_make = models.ForeignKey(Make, on_delete=models.CASCADE)
    registration_no = models.CharField(max_length=15)
    v_model = models.ForeignKey(V_model, on_delete=models.CASCADE)
    vin_no = models.CharField(max_length=100)
    engine_no = models.CharField(max_length=100)
    service_intervall = models.ForeignKey(Service_Interval, on_delete=models.CASCADE)
    last_service  = models.IntegerField()
    current_milage = models.IntegerField()

    def __str__(self):
        return str(self.v_model) + " " + self.registration_no

# 'name', 'phone', 'email', 'address', 'postal', 'area'
class Company(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    postal = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
    
class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    serviced_vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
    service_date = models.DateField()
    service_type = models.CharField(max_length=50)
    serviced_at = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return str(self.service_type) + " " + str(self.serviced_vehicle)
    



