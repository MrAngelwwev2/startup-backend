"""startup_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import CategoriesListView, CarreersListView, CountryListView, MetodologyListView, SoftwareListView, ChargesListView, CitiesListView, SkillsListView, CertificationListView, CreateUserView, LoginView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('categories/', CategoriesListView.as_view(), name='categories-list'),
    path('carreers/', CarreersListView.as_view(), name='carreers-list'),
    path('countries/', CountryListView.as_view(), name='countries-list'),
    path('methodologies/', MetodologyListView.as_view(), name='methodologies-list'),
    path('softwares/', SoftwareListView.as_view(), name='methodologies-list'),
    path('charges/carreers/<int:id_carreers>/', ChargesListView.as_view(), name='charges-by-carreers'),
    path('cities/country/<int:id_country>/', CitiesListView.as_view(), name='cities-by-country'),
    path('certifications/carreers/<int:id_carreers>/', CertificationListView.as_view(), name='certifications-by-carreers'),
    path('skills/carreers/<int:id_carreers>/', SkillsListView.as_view(), name='skills-by-carreers'),
    path('users/create/', CreateUserView.as_view(), name='create-user'),
    path('login/', LoginView.as_view(), name='login'),
]
