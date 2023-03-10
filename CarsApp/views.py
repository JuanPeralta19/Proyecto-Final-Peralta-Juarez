from django.shortcuts import render
from CarsApp.models import Americano, Europeo, Japones

def index(request):
    return render(request,"CarsApp/index.html")

def template_herencia(request):
    americanos = Americano.objects.all()
    return render(request, "CarsApp/otro-template.html", {"americanos": americanos})
