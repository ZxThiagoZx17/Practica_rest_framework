"""
URL configuration for practica_rest_framework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

#Definen y organizan rutas de las aplicaciones
from django.urls import path, include

#Generean automaticamente las rutas de los viewsets
from rest_framework import routers

#Importamos vistas creadas previamente
from API import views

#Creamos un router para el manejo de rutas para los viewsets, tambien nos da un GUI para navegar en la API 
router = routers.DefaultRouter()

#Asociamos las rutas para las vistas que importamos, User y Group
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    #Incluye todas las rutas generadas por router desde la raiz de la app asi: "GET /users/": Lista todos los usuarios.
    path('', include(router.urls)),

    #Incluye URLs de autenticacion y prefijo para ingresar a la API, añade funcionalidades de login y logout
    #la url iria api-autenticacion/login-logout
    path('api-autenticacion/', include('rest_framework.urls', namespace='rest_framework'))
]
