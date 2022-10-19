from rest_framework import serializers
from client.models import Client
from car.models import Car
from company.models import Company


class clientserializer(serializers.Serializer):
    class Meta:
        model = Client
        field = '__all__'


class carserializer(serializers.Serializer):
    class Meta:
        model = Car
        field = '__all__'


class companyserializer(serializers.Serializer):
    class Meta:
        model = Company
        field = '__all__'
