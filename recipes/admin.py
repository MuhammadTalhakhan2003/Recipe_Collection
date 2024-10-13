from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'ingredients', 'created_at')  # Ensure you only include fields that exist

admin.site.register(Recipe, RecipeAdmin)
