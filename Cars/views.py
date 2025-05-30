from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from Cars.models import Cars
from django.contrib.auth import logout


def mainPage(request):
    Car = Cars.objects.all().values()
    template = loader.get_template('MainPage.html')
    context = {
        'Car': Car,
    }
    return HttpResponse(template.render(context, request))


def Panel(request):
    Car = Cars.objects.all().values()
    template = loader.get_template('Cars.html')
    context = {
        'Car': Car,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def About(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render({}, request))


def Contact(request):
    template = loader.get_template('Contact.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    Name = request.POST['Name']
    FuelType = request.POST['FuelType']
    PhotoLink = request.POST['PhotoLink']
    Acceleration = request.POST['Acceleration']
    TopSpeed = request.POST['TopSpeed']
    TotalPower = request.POST['TotalPower']
    TotalTorque = request.POST['TotalTorque']
    Drive = request.POST['Drive']
    CarBody = request.POST['CarBody']
    FeulEconomy = request.POST['FeulEconomy']
    Car = Cars(Name=Name, FuelType=FuelType, PhotoLink=PhotoLink,
               Acceleration=Acceleration, TopSpeed=TopSpeed, TotalPower=TotalPower,
               TotalTorque=TotalTorque, Drive=Drive, CarBody=CarBody, FeulEconomy=FeulEconomy)
    Car.save()
    return HttpResponseRedirect(reverse('Panel'))


def delete(request, id):
    Car = Cars.objects.get(id=id)
    Car.delete()
    return HttpResponseRedirect(reverse('Panel'))


def update(request, id):
    Car = Cars.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'Car': Car,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    Name = request.POST['Name']
    FuelType = request.POST['FuelType']
    PhotoLink = request.POST['PhotoLink']
    Acceleration = request.POST['Acceleration']
    TopSpeed = request.POST['TopSpeed']
    TotalPower = request.POST['TotalPower']
    TotalTorque = request.POST['TotalTorque']
    Drive = request.POST['Drive']
    CarBody = request.POST['CarBody']
    FeulEconomy = request.POST['FeulEconomy']
    Car = Cars.objects.get(id=id)
    Car.Name = Name
    Car.FuelType = FuelType
    Car.PhotoLink = PhotoLink
    Car.Acceleration = Acceleration
    Car.TopSpeed = TopSpeed
    Car.TotalPower = TotalPower
    Car.TotalTorque = TotalTorque
    Car.Drive = Drive
    Car.CarBody = CarBody
    Car.FeulEconomy = FeulEconomy

    Car.save()
    return HttpResponseRedirect(reverse('Panel'))


def logout(request):

    return HttpResponseRedirect(reverse('login'))
