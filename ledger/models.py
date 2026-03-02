from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse('user', args=[str(self.pk)])

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.ingredientName}'
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.pk)])

class Recipe(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'users')
    recipeName = models.CharField(max_length=100)
    createdOn = models.DateTimeField(auto_now_add=True) 
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.recipeName}'
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name = 'recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name = 'ingredients')
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.pk)])


# Create your models here.
