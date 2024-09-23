from rest_framework import serializers
from .models import Categories, Carreers, Country, Metodology, Softwares

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id_categories', 'category']


class CarreersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreers
        fields = ['id_carreers', 'carreer']
        
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id_country', 'country']

class MetodologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodology
        fields = ['id_metodology', 'metodology']
        
class SoftwaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwares
        fields = ['id_softwares', 'software']