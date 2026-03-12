from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

from django.contrib import admin
from .models import Profile, Recipe, RecipeIngredient, RecipeImage

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

class RecipeIngriedientInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    search_fields = ('recipe', )
    model = Recipe 
    inlines = [RecipeIngriedientInLine, RecipeImageInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)