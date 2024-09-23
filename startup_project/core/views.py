from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Categories, Carreers, Country, Metodology, Softwares, Charges, Cities, Skills, Users, Certification
from .serializers import CategoriesSerializer, CarreersSerializer, CountrySerializer, MetodologySerializer, SoftwaresSerializer, ChargesSerializer, CitiesSerializer, SkillsSerializer, CertificationSerializer, UsersSerializer

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
    
# Vista para obtener los cargos filtradas por carrera
class ChargesListView(APIView):
    def get(self, request, id_carreers):
        charges = Charges.objects.filter(id_carreers=id_carreers)
        if not charges.exists():
            return Response({"detail": "No se encontraron cargos para esta carrera."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ChargesSerializer(charges, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Vista para obtener las ciudades filtradas por país
class CitiesListView(APIView):
    def get(self, request, id_country):
        cities = Cities.objects.filter(id_country=id_country)
        if not cities.exists():
            return Response({"detail": "No se encontraron ciudades para este país."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CitiesSerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Vista para obtener las certificaciones filtradas por carrera
class CertificationListView(APIView):
    def get(self, request, id_carreers):
        certification = Certification.objects.filter(id_carreers=id_carreers)
        if not certification.exists():
            return Response({"detail": "No se encontraron certificaciones para esta carrera."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CertificationSerializer(certification, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Vista para obtener las skills filtradas por carrera
class SkillsListView(APIView):
    def get(self, request, id_carreers):
        skills = Skills.objects.filter(id_carreers=id_carreers)
        if not skills.exists():
            return Response({"detail": "No se encontraron ciudades para este país."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SkillsSerializer(skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Guardar el nuevo usuario
class CreateUserView(APIView):
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Inicio de sesión
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Se requiere email y contraseña."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        if check_password(password, user.password):
            return Response({"message": "Login exitoso", "user_id": user.id_users}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Correo o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)