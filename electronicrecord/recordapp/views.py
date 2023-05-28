from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
@api_view(['GET'])
def getClient(request):

    client = Client.objects.all()

    srlz = ClientSerializer(client, many=True)

    return Response(srlz.data)

