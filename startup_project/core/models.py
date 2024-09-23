from django.db import models

# Create your models here.
class Carreers(models.Model):
    id_carreers = models.AutoField(primary_key=True)
    carreer = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'carreers'


class Categories(models.Model):
    id_categories = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'categories'


class Certification(models.Model):
    id_certification = models.AutoField(primary_key=True)
    id_carreers = models.ForeignKey(Carreers, models.DO_NOTHING, db_column='id_carreers')
    certification = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'certification'


class Charges(models.Model):
    id_charges = models.AutoField(primary_key=True)
    id_carreers = models.ForeignKey(Carreers, models.DO_NOTHING, db_column='id_carreers')
    charges = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'charges'


class Cities(models.Model):
    id_cities = models.AutoField(primary_key=True)
    id_country = models.ForeignKey('Country', models.DO_NOTHING, db_column='id_country')
    city = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cities'

class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'country'


class Metodology(models.Model):
    id_metodology = models.AutoField(primary_key=True)
    metodology = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'metodology'


class Skills(models.Model):
    id_skills = models.AutoField(primary_key=True)
    id_carreers = models.ForeignKey(Carreers, models.DO_NOTHING, db_column='id_carreers')
    skill = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'skills'


class Softwares(models.Model):
    id_softwares = models.AutoField(primary_key=True)
    software = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'softwares'


class Users(models.Model):
    id_users = models.AutoField(primary_key=True)
    names = models.CharField(max_length=256)
    last_names = models.CharField(max_length=256)
    email = models.CharField(max_length=180)
    born_date = models.DateField()
    personal_identification_number = models.IntegerField()
    phone_number = models.CharField(max_length=16)
    gender = models.CharField(max_length=50)
    id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='id_country')
    id_cities = models.ForeignKey(Cities, models.DO_NOTHING, db_column='id_cities')
    password = models.CharField(max_length=256)
    url_linkedin = models.CharField(max_length=180)
    id_carreers = models.ForeignKey(Carreers, models.DO_NOTHING, db_column='id_carreers', blank=True, null=True)
    id_skills = models.ForeignKey(Skills, models.DO_NOTHING, db_column='id_skills', blank=True, null=True)
    id_certification = models.ForeignKey(Certification, models.DO_NOTHING, db_column='id_certification', blank=True, null=True)
    id_softwares = models.ForeignKey(Softwares, models.DO_NOTHING, db_column='id_softwares', blank=True, null=True)
    id_metodology = models.ForeignKey(Metodology, models.DO_NOTHING, db_column='id_metodology', blank=True, null=True)
    id_charges = models.ForeignKey(Charges, models.DO_NOTHING, db_column='id_charges', blank=True, null=True)
    id_categories = models.ForeignKey(Categories, models.DO_NOTHING, db_column='id_categories', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'