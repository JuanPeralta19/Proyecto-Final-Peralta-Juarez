from django.shortcuts import render
from CarsApp.models import vehiculos
from CarsApp.forms import vehiculosForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

def index(request):
    return render(request,"CarsApp/index.html")


def mostrar_vehiculos(request):
    context = {
        "form":vehiculosForm(),
        "vehiculos":vehiculos.objects.all()}
    return render(request, "CarsApp/admin_vehiculos.html", context)

def agregar_vehiculos(request):
    vehiculos_form = vehiculosForm(request.POST)
    vehiculos_form.save()
    context = {
        "form": vehiculosForm(),
        "vehiculos":vehiculos.objects.all()
    }
    return render(request,"CarsApp/admin_vehiculos.html",context)

def buscar_vehiculos(request):
    criterio = request.GET.get("criterio")
    context = {
        "vehiculos": vehiculos.objects.filter(marca_de_vehiculo__icontains=criterio).all(),
    }
    return render(request,"CarsApp/admin_vehiculos.html", context)

class VehiculosList(ListView):
    model = vehiculos
    context_object_name = "vehiculos"

class VehiculosDetail(DetailView):
    model = vehiculos
    context_object_name = "vehiculo"