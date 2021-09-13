from django.db import models
from recipe_scrapers import timesofindia
from django.contrib.auth.models import User

# models represets data django stores inside of a database
# one class= a table wher you store reltaed info
# create a migration to tell django what to do to the databse
# migrateion step to take instruction and apply them to database

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    serving = models.CharField(max_length=15)
    time = models.IntegerField()
    url = models.URLField()
    image = models.URLField(blank=True, null=True, default="https://st4.depositphotos.com/14953852/24787/v/600/depositphotos_247872612-stock-illustration-no-image-available-icon-vector.jpg")
    ingredients = models.TextField(default="")
    directions = models.TextField(default="")

    def __str__(self):
        return self.name


class RecipeShelf(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe, blank=True)

    def __str__(self):
        return "Test"
        #return "%s\'s recipe shelf" % self.user