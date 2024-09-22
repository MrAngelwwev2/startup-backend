from rest_framework import serializers
from .models import Categories, Carreers

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id_categories', 'category']


class CarreersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreers
        fields = ['id_carreers', 'carreer']
