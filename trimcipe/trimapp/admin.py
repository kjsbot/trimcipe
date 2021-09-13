from django.contrib import admin

from .models import Recipe, RecipeShelf

# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeShelf)