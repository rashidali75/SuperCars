from django.shortcuts import render
from . import views
from page.models import Team


def home(request):
    team = Team.objects.all()
    return render(request, 'pages/home.html',{'team':team})


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')

# def cars(request):
#     return render(request, 'cars/cars.html')