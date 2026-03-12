"""
URL configuration for recipebook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from .views import RecipesDetailView, RecipesListView, RecipeCreateView, RecipeImageCreateView

urlpatterns = [
    path('recipes/list', RecipesListView.as_view(), name='recipes-list'),
    path('recipe/<int:pk>', RecipesDetailView.as_view(), name='recipe-detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/add_image', RecipeImageCreateView.as_view(), name='recipe-image-add')
]

app_name = "ledger"
