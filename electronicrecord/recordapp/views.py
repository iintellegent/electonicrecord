from django.http import JsonResponse
import json
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
    #return JsonResponse({})
    return Response(data=srlz.data)
@api_view(['POST'])
def add_client(request):
    try:
        data = json.loads(request.body.decode())

        client_id = uuid.uuid4()

        client = Client.objects.create(
            id=client_id)
        client.Surname = data["surname"]
        client.Name = data["name"]
        client.Patronic = data["patronic"]

        client.save()

        return JsonResponse ({
            'id': client_id
        })
    except:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса.'}, status=400)

@api_view(['GET'])
def get_specialist(request):

    specialist = Specialist.objects.all()

    srlz = SpecialistSerializer(specialist, many=True)
    # return JsonResponse({})
    return Response(data=srlz.data)

@api_view(['POST'])
def add_specialist(request):
    try:
        data = json.loads(request.body.decode())

        specialist_id = uuid.uuid4()

        specialist = Specialist.objects.create(
            id=specialist_id)
        specialist.Surname = data["surname"]
        specialist.Name = data["name"]
        specialist.Patronic = data["patronic"]

        specialist.save()

        return JsonResponse({
                'id': specialist_id
            })
    except:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса.'}, status=400)