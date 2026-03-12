from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Recipe, RecipeImage
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeForm, RecipeImageForm
# Create your views here.


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'


class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe.html'
    context_object_name = 'recipe'

class RecipeCreateView(LoginRequiredMixin,CreateView):
    model = Recipe
    # fields = '__all__'
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = '/recipes/list'

class RecipeImageCreateView(LoginRequiredMixin,CreateView):
    model = RecipeImage
    # fields = '__all__'
    form_class = RecipeImageForm
    template_name = 'recipes/recipe_form.html'
    success_url = '/recipes/list'
