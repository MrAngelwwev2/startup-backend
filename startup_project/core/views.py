from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import Categories, Carreers
from serializers import CategoriesSerializer, CarreersSerializer

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