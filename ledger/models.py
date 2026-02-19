from django.db import models

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.ingredientName}'
    
    def get_absolute_url(self):
        return reverse('recipes/list', args=[str(self.name)])

class Recipe(models.Model):
    recipeName = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.recipeName}'
    
    def get_absolute_url(self):
        return reverse('recipes/list', args=[str(self.name)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name = 'ingredients')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name = 'recipe')
    
    def get_absolute_url(self):
        return reverse('recipes/list', args=[str(self.name)])

# Create your models here.
