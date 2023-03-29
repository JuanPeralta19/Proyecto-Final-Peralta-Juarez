#  Sitio Web de Python Djando AutosPedia.comm 
---
[![N|Solid](https://www.milinux.es/wp-content/uploads/2019/01/python-256x256.png)](https://nodesource.com/products/nsolid) [![N|Solid](https://cdn.iconscout.com/icon/free/png-256/django-11-1175036.png)](https://nodesource.com/products/nsolid) 

### Descripcion
---
Sitio web de fanaticos de autos donde podran subir su vehiculo favorito ingresando la marca del mismo y su modelo, tambien podran especificar el motor que posee ese vehiculo, una breve descripcion y el origen del fabricante. Esta pagina esta realizada con Python y su framework django.

### Dependencias
---

    Python 3.11.1           | Lenguaje de programación utilizado en el proyecto.
    Bootstrap 5.3           | Agregue template a mi pagina web.
    Django 4.1.7            | Framework utilizado para la creación del sitio web.  
---


### Implementaciones Tercera pre-entrega
---
- [x] Herencia de HTML.
- [x] 3 clases en models.
- [x] Formulario para insertar datos en cada una de las clases
- [x] Formulario que accede y trae info de la base de datos.
- [x] Archivo seed_data.py con datos para testear el sitio web.
- [x] Agregar botones que redireccionen a otras vistas.
- [x] Implentacion de Login y Logout de usuario.

### Bullet-NavBar estando logueado.
- En el boton "inicio" ubicado en el NavBar presento la vista con todas las publicaciones subidas y sus respectivos botones "detalles", "actualizar" y "borrar".
- En el boton Vehículos presento una vista con un listado de los vehiculos, con tres atributos solamente, y los botones anteriormente nombrados, detalles, actualizar y borrar.
- En el boton "Mis publicaciones" presento una vista con el listado de las publicaciones realizadas por el perfil ingresado.
- En el boton "Crear publicacion" presento una vista con un formulario de creacion para poder subir publicaciones.
- El boton "Perfil" es de tipo "dropdown" que contiene otros dos botones "Actualizar/Crear Avatar" y "Nombre de usuario |Salir"
- el boton "Mensajes" es de tipo "dropdown" que contiene un boton para ver mensajes, "Mis mensajes" y otro boton para enviar mensajes, "Enviar mensaje".
- El ultimo boton "Acerca de mi" presenta una vista contando un poco sobre el creador de la pagina, sus motivaciones y agradecimiento.
- Utilizando el buscador se podra filtar todos los vehiculos por marca.

---
### Bullet-Navbar sin estar logueado.
- En el boton "inicio" ubicado en el NavBar presento la vista con todas las publicaciones subidas y el boton "detalles" ya que al no estar logueado no esta autorizado para realizar las acciones de actualizar y borrar la publicacion.
- En el boton Vehículos presento una vista con un listado de los vehiculos, con tres atributos solamente. Se muestra solo el boton "Detalles".
- El boton "Cuenta" es de tipo "dropdown" que contiene un boton "Ingresar" donde te pide nombre de usuario y contraseña. Y otro boton "Registrarme" donde te pida nombre de usuario y contraseña.
- El ultimo boton "Acerca de mi" presenta una vista contando un poco sobre el creador de la pagina, sus motivaciones y agradecimiento.
-  Utilizando el buscador se podra filtar todos los vehiculos por marca.