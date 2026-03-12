from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
    recipeName = forms.CharField(label='Recipe Name', max_length=100)

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'
    image = forms.ImageField(label='Image')
    description = forms.CharField(label='Description', max_length=255)