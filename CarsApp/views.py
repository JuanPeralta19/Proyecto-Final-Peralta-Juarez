from django.shortcuts import render
from CarsApp.models import Americano, Europeo, Japones
from CarsApp.forms import AmericanoForm, EuropeoForm, JaponesForm

def index(request):
    return render(request,"CarsApp/index.html")

def template_herencia(request):
    americanos = Americano.objects.all()
    return render(request, "CarsApp/otro-template.html", {"americanos": americanos})

def mostrar_vehiculos_americanos(request):
    context = {
        "form":AmericanoForm(),
        "americanos":Americano.objects.all()}
    return render(request, "CarsApp/admin_vehiculos.html", context)

def agregar_vehiculos_americanos(request):
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

#VEHICULOS EUROPEOS

def mostrar_vehiculos_europeos(request):
      context = {
          "form": EuropeoForm,
          "europeos": Europeo.objects.all(),
      }
      return render(request, "CarsApp/admin_vehiculos_europeos.html", context)

def agregar_vehiculo_europeo(request):
    europeo_form = EuropeoForm(request.POST)
    europeo_form.save()
    context = {
        "form":EuropeoForm(),
        "europeos": Europeo.objects.all(),
    }
    return render(request,"CarsApp/admin_vehiculos_europeos.html", context)

def buscar_vehiculo(request):
    criterio = request.GET.get("criterio")
    context = {
        "europeos": Europeo.objects.filter(marca_de_vehiculo__icontains=criterio).all(),
    }
    return render(request, "CarsApp/admin_vehiculos_europeos.html",context)

# VEHICULOS JAPONESES

def mostrar_vehiculos_japoneses(request):
      context = {
          "form": JaponesForm,
          "japones": Japones.objects.all(),
      }
      return render(request, "CarsApp/admin_vehiculos_japoneses.html", context)

def agregar_vehiculo_japones(request):
    japones_form = JaponesForm(request.POST)
    japones_form.save()
    context = {
        "form":JaponesForm(),
        "Japones": Japones.objects.all(),
    }
    return render(request,"CarsApp/admin_vehiculos_japoneses.html", context) 


