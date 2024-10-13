from django.shortcuts import render, get_object_or_404
from .models import Recipe

def index(request):
    recipes = Recipe.objects.all()  # Get all recipes
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)  # Get a recipe by ID
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
