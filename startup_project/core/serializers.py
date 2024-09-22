from rest_framework import serializers
from .models import Categories, Carreers, Countries

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id_categories', 'category']


class CarreersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreers
        fields = ['id_carreers', 'carreer']
        
class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['id_countries', 'country']
