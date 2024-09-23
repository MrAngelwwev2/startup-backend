from rest_framework import serializers
from .models import Categories, Carreers, Country, Metodology, Softwares, Charges, Cities, Skills, Users, Certification

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
        
class ChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charges
        fields = ['id_charges', 'charges', 'id_carreers']
        
class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['id_cities', 'city', 'id_country']

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['id_skills', 'skill', 'id_carreers']
        
class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id_certification', 'certification', 'id_carreers']