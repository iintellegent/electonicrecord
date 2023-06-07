from rest_framework import serializers
from .models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id',
                   'Surname',
                   'Name',
                   'Patronic')

class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ('id',
                   'Surname',
                   'Name',
                   'Patronic')