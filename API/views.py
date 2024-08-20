from django.shortcuts import render

#Importamos las tablas Group y User de la base de datos (Group y User ya estan predefinidos en Django).
from django.contrib.auth.models import Group, User

#permissions incluye funciones para manejar la restriccion al acceso de recursos.
#viewsets agrupa la logica relacionada de las vistas, en lugar de definir varias vistas para crear, actualizar y eliminar elementos, viewsets permite realizar operaciones CRUD con una sola clase. 
from rest_framework import permissions, viewsets

#Serializadores creados previamente
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

# Create your views here.
"""
ModelViewSet es una subclase que nos permite acciones como:

list: Obtener una lista de todos los objetos.
retrieve: Obtener un único objeto por su ID.
create: Crear un nuevo objeto.
update: Actualizar un objeto existente.
partial_update: Actualizar parcialmente un objeto existente.
destroy: Eliminar un objeto.

Esto se asemeja a la funcion que hace "Router" en urls.py:
GET /users/: Lista todos los usuarios.
POST /users/: Crea un nuevo usuario.
GET /users/{id}/: Obtiene un usuario por su ID.
PUT /users/{id}/: Actualiza un usuario existente.
PATCH /users/{id}/: Actualiza parcialmente un usuario.
DELETE /users/{id}/: Elimina un usuario.

Todo esto se hace detras de escena
"""


#Clase que nos permite realizar operaciones CRUD con USER
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #Selecciona todos los usuarios en la bse de datos y los ordena por la fecha de creacion en orden descendente
    queryset = User.objects.all().order_by('-date_joined')

    #Escojemos el serializador utilizado para convertir datos a JSON/XML 
    serializer_class = UserSerializer

    #Esta linea define que solo usuarios autenticados puede acceder a esta vista/endpoint API
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]