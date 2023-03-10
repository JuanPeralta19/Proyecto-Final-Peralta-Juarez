from django.shortcuts import render
from CarsApp.models import Americano, Europeo, Japones
from CarsApp.forms import AmericanoForm

def index(request):
    return render(request,"CarsApp/index.html")

def template_herencia(request):
    americanos = Americano.objects.all()
    return render(request, "CarsApp/otro-template.html", {"americanos": americanos})

def mostrar_vehiculos(request):
    context = {
        "form":AmericanoForm(),
        "americanos":Americano.objects.all()}
    return render(request, "CarsApp/admin_vehiculos.html", context)

def agregar_vehiculos(request):
    americano_form = AmericanoForm(request.POST)
    americano_form.save()
    context = {
        "form": AmericanoForm(),
        "americanos":Americano.objects.all()
    }
    return render(request,"CarsApp/admin_vehiculos.html",context)

def buscar_vehiculo(request):
    criterio = request.GET.get("criterio")
    context = {
        "americanos": Americano.objects.filter(marca_de_vehiculo__icontains=criterio).all(),
    }
    return render(request, "CarsApp/admin_vehiculos.html",context)    
