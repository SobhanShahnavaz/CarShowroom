from django.db import models


class Cars(models.Model):
    Name = models.CharField(max_length=127)
    FuelType = models.CharField(max_length=127, default="Petrol")
    PhotoLink = models.TextField(default="/")
    Acceleration = models.CharField(max_length=127, default="10.10 sec")
    TopSpeed = models.CharField(max_length=127, default="200 mph")
    TotalPower = models.CharField(max_length=127, default="200 hp")
    TotalTorque = models.CharField(max_length=127, default="200 nm")
    Drive = models.CharField(max_length=127, default="AWD")
    CarBody = models.CharField(max_length=127, default="Sport")
    FeulEconomy = models.CharField(max_length=127, default="16")
