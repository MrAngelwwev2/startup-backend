from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Categories, Carreers, Country, Metodology, Softwares
from .serializers import CategoriesSerializer, CarreersSerializer, CountrySerializer, MetodologySerializer, SoftwaresSerializer

# Create your views here.
class CategoriesListView(APIView):
    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Vista para obtener todas las carreras
class CarreersListView(APIView):
    def get(self, request):
        carreers = Carreers.objects.all()
        serializer = CarreersSerializer(carreers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Vista para obtener todos los países
class CountryListView(APIView):
    def get(self, request):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Vista para obtener todas las metodologías
class MetodologyListView(APIView):
    def get(self, request):
        metodology = Metodology.objects.all()
        serializer = MetodologySerializer(metodology, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Vista para obtener todos los softwares
class SoftwareListView(APIView):
    def get(self, request):
        software = Softwares.objects.all()
        serializer = SoftwaresSerializer(software, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)