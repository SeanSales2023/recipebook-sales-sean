from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import RecipeIngredient

# Create your views here.

def recipes_list(request):
    recipe1 = RecipeIngredient.objects.filter(recipe__recipeName__exact='Recipe 1')
    recipe2 = RecipeIngredient.objects.filter(recipe__recipeName__exact='Recipe 2')
    recipe1ingredients = RecipeIngredient.objects.filter(recipe__recipeName='Recipe 1')
    recipe2ingredients = RecipeIngredient.objects.filter(recipe__recipeName='Recipe 2')
    ctx =  {
    'recipe1': recipe1,
    'recipe2': recipe2,
    'recipe2ingredients': recipe1ingredients,
    'recipe2ingredients': recipe2ingredients,
    }
    return render(request, "recipes/recipes_list.html", ctx)

def recipe1(request):
    recipe = RecipeIngredient.objects.filter(recipe__name='Recipe 1')
    ingredients = RecipeIngredient.objects.filter(recipe__recipeName='Recipe 1')
    ctx = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'recipes/recipe.html', ctx)

def recipe2(request):
    recipe = RecipeIngredient.objects.filter(recipe__name='Recipe 2')
    ingredients = RecipeIngredient.objects.filter(recipe__recipeName='Recipe 2')
    ctx = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'recipes/recipe.html', ctx)