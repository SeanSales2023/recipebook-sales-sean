from django.db import models

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.ingredientName}'
    
    def get_absolute_url(self):
        return reverse('ingredients', args=[str(self.pk)])

class Recipe(models.Model):
    recipeName = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.recipeName}'
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name = 'recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name = 'ingredients')
    
    def get_absolute_url(self):
        return reverse('recipe_ingredient', args=[str(self.pk)])

# Create your models here.
