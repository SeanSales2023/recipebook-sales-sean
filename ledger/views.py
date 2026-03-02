from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required

# Create your views here.

def recipes_list(request):
    recipe1 = Recipe.objects.get(recipeName__exact='Recipe 1')
    recipe2 = Recipe.objects.get(recipeName__exact='Recipe 2')
    ctx =  {
    'recipe1': recipe1,
    'recipe2': recipe2, 
    }
    return render(request, "recipes/recipes_list.html", ctx)

@login_required
def recipe1(request):
    recipe = Recipe.objects.get(recipeName='Recipe 1')
    items = RecipeIngredient.objects.filter(recipe__recipeName='Recipe 1')
    ctx = {
        'recipe': recipe,
        'items': items
    }
    return render(request, 'recipes/recipe.html', ctx)

@login_required
def recipe2(request):
    recipe = Recipe.objects.get(recipeName='Recipe 2')
    items = RecipeIngredient.objects.filter(recipe__recipeName='Recipe 2')
    ctx = {
        'recipe': recipe,
        'items': items
    }
    return render(request, 'recipes/recipe.html', ctx)