from django.shortcuts import render
from CarsApp.models import vehiculos , perfil, mensaje
from CarsApp.forms import vehiculosForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    vehiculo = vehiculos.objects.all().order_by("-fecha_creacion")
    return render(request,"CarsApp/index.html", {"vehiculos":vehiculo})

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
     
class VehiculosUpdate(LoginRequiredMixin ,PermitsOnlyOwners, UpdateView):
    model = vehiculos
    success_url = reverse_lazy("vehiculos-mine")
    fields = "__all__"

class VehiculosDelete(LoginRequiredMixin, PermitsOnlyOwners, DeleteView):
    model = vehiculos
    context_object_name = "vehiculo"
    success_url = reverse_lazy("index")

   
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

class PerfilCreate(LoginRequiredMixin, CreateView):
    model = perfil
    success_url = reverse_lazy('index')
    fields = ['avatar']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PerfilUpdate(UserPassesTestMixin, UpdateView):
    model = perfil
    success_url = reverse_lazy('index')
    fields = ['avatar',]

    def test_func(self):
        return perfil.objects.filter(user = self.request.user).exists()
    
class MensajeCreate(CreateView):
    model = mensaje
    success_url = reverse_lazy('mensaje-create')
    fields = "__all__"

class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy('mensaje-list')

    def test_func(self):
        return mensaje.objects.filter(destinatario = self.request.user).exists()

class MensajeList(LoginRequiredMixin, ListView):
    model = mensaje
    context_object_name = "mensaje"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return mensaje.objects.filter(destinatario=self.request.user).all()



