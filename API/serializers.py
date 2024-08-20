#El archivo serializers.py sirve para convertir datos de tipo modelo, conjuntos de consultas en tipos de datos nativos en python con JSON o XML para trabajar de la mano con frontend 

#Los seriadores tambien proporcionan deserializadores lo cual hace el proceso inverso, JSON/XML a instancias de modelos despues de validar las entradas 

#Datos extraidos de modelos creados
from django.contrib.auth.models import Group, User 
#Libreria con herramientas para serializar/deserializar
from rest_framework import serializers

#Clase serializador del modelo/tabla User con "HyperlinkedModelSerializer" para representacion de datos sin negar que hay mas opciones
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #Tabla/modelo a serializar
        model = User
        #Atributos a serializar
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']