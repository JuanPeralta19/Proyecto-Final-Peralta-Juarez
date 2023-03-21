from django.shortcuts import render
from CarsApp.models import vehiculos
from CarsApp.forms import vehiculosForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,"CarsApp/index.html")

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

class VehiculosUpdate(UpdateView):
    model = vehiculos
    success_url = reverse_lazy("vehiculos-list")
    fields = "__all__"

class VehiculosDelete(DeleteView):
    model = vehiculos
    context_object_name = "vehiculo"
    success_url = reverse_lazy("vehiculos-list")

class VehiculosCreate(CreateView):
    model = vehiculos
    success_url = reverse_lazy("vehiculos-list")
    fields = "__all__"

class VehiculosSearch(ListView):
    model = vehiculos
    context_object_name = "vehiculos"
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = vehiculos.objects.filter(marca_de_vehiculo__icontains=criterio).all()
        return result
    
class Login(LoginView):
    next_page = reverse_lazy("index")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("index")

class Logout(LogoutView):
    template_name= "registration/logout.html"
