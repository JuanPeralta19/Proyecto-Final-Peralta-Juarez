from django.shortcuts import render
from CarsApp.models import vehiculos
from CarsApp.forms import vehiculosForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class VehiculosMineList(LoginRequiredMixin, VehiculosList):
    def get_queryset(self):
        return vehiculos.objects.filter(publicador = self.request.user.id).all()

class VehiculosDetail(DetailView):
    model = vehiculos
    context_object_name = "vehiculo"

class PermitsOnlyOwners(UserPassesTestMixin):
    def test_func(self):
        user_id = self.request.user.id
        vehiculos_id = self.kwargs.get("pk")
        return vehiculos.objects.filter(publicador = user_id, id = vehiculos_id).exists()
     
class VehiculosUpdate(LoginRequiredMixin,PermitsOnlyOwners, UpdateView):
    model = vehiculos
    success_url = reverse_lazy("vehiculos-mine")
    fields = "__all__"

class VehiculosDelete(LoginRequiredMixin,PermitsOnlyOwners, DeleteView):
    model = vehiculos
    context_object_name = "vehiculo"
    success_url = reverse_lazy("vehiculos-list")

   
class VehiculosCreate(LoginRequiredMixin, CreateView):
    model = vehiculos
    success_url = reverse_lazy("vehiculos-mine")
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
