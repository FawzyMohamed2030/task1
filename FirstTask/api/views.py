from rest_framework.response import Response
from rest_framework.decorators import api_view
from client.models import Client
from company.models import Company
from car.models import Car
from .serializers import clientserializer, carserializer, companyserializer


@api_view(['GET'])
def getclient(request):
    x = Client.objects.all()
    serial = clientserializer(x, many=True)
    return Response(serial.data)


@api_view(['GET'])
def getcar(request):
    x = Car.objects.all()
    serial = carserializer(x, many=True)
    return Response(serial.data)


@api_view(['GET'])
def getcompany(request):
    x = Company.objects.all()
    serial = companyserializer(x, many=True)
    return Response(serial.data)
