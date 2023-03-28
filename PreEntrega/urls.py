"""PreEntrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CarsApp.views import (index, VehiculosList, VehiculosDetail, VehiculosUpdate, VehiculosDelete, 
                           VehiculosCreate, VehiculosSearch, VehiculosMineList, Login, SignUp, Logout, PerfilCreate, PerfilUpdate,
                           MensajeCreate, MensajeDelete, MensajeList, About)
from django.conf import settings
from django.conf.urls.static import static
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('Vehiculos/List', VehiculosList.as_view(), name = "vehiculos-list"),
    path('Vehiculos/Mine/List', VehiculosMineList.as_view(), name = "vehiculos-mine"),
    path('Vehiculos/<pk>/Detail', VehiculosDetail.as_view(), name = "vehiculos-detail"),
    path('Vehiculos/<pk>/Update', VehiculosUpdate.as_view(), name = "vehiculos-update"),
    path('Vehiculos/<pk>/Delete', VehiculosDelete.as_view(), name = "vehiculos-delete"),
    path('Vehiculos/Create', VehiculosCreate.as_view(), name = "vehiculos-create"),
    path('Vehiculos/Search', VehiculosSearch.as_view(), name = "vehiculos-search"),
    path('login/', Login.as_view(), name = "login"),
    path('signup/', SignUp.as_view(), name = "signup"),
    path('logout/', Logout.as_view(), name = "logout"),
    path('Perfil/Create', PerfilCreate.as_view(), name="perfil-create"),
    path('Perfil/<pk>/Update', PerfilUpdate.as_view(), name="perfil-update"),
    path('Mensaje/Create', MensajeCreate.as_view(), name="mensaje-create"),
    path('Mensaje/<pk>/Delete', MensajeDelete.as_view(), name = "mensaje-delete"),
    path('Mensaje/List', MensajeList.as_view(), name = "mensaje-list"),
    path('About/', About, name = "acerca-de-mi"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

