from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.db import IntegrityError
from recipe_scrapers import scrape_me
from recipe_scrapers import WebsiteNotImplementedError
from .forms import TrimRecipe
from .models import Recipe, RecipeShelf, User

def index(request):
    form = TrimRecipe()
    context = {'form' : form}
    return render(request, "trimapp/index.html", context)



def recipe(request):
    form = TrimRecipe(request.POST) # adds all POST data text into form
    context = {}

    if form.is_valid():
        try:
            recipeUrl = request.POST["url"]
        except WebsiteNotImplementedError:
            return render(request, "trimapp/index.html", {
                "message": "You've entered an invalid URL!"
            })

        scraper = scrape_me(recipeUrl)
        image = scraper.image()
        title = scraper.title()
        serving = scraper.yields()
        time = scraper.total_time()
        ingredients = scraper.ingredients()
        instructions = scraper.instructions().splitlines()

        recipe = Recipe(name=title, serving=serving, time=time, url=recipeUrl, image=image, ingredients=ingredients, directions=instructions)
        recipe.save()

        context = {"title" : title, "serving" : serving, "time" : time, "url" : recipeUrl, "ingredients" : ingredients, "instructions" : instructions} #add ingredeints and other shit later
        return render(request, "trimapp/recipe.html", context)
    else:
        return render(request, "trimapp/index.html", {"form" : form})



# def save_recipe(request)
# function; if click save
# get id of recipe and get id of user's recipe shelf
# add the recipe to recipe shelf
# 
# 
# context = {"success" : "Recipe saved!"}
# return render(request, "trimapp/recipe.html", context)



def shelf(request):
    user_shelf = RecipeShelf.objects.get(id=2) #get the user's unique shelf by ID
    shelf_recipes = user_shelf.recipes.all() #get each recipe inside the shelf
    amnt_of_recipes = user_shelf.recipes.count() #returns how many recipes are in the user's shelf
    context = {"recipes" : shelf_recipes, "amount" : amnt_of_recipes}

    return render(request, "trimapp/shelf.html", context)

    # user = User.objects.get(id=1)
    # recipes = user.RecipeShelf_set.all()



def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "trimapp/login.html", {"message" : "Invalid username and/or password!" })
    else:
        return render(request, "trimapp/login.html")
        


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username=username, password=password)
            user_shelf = RecipeShelf(user=request.user.id)
            user_shelf.save()
        except IntegrityError:
            return render(request, "trimapp/register.html", {
                "message": "Username is already taken!"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "trimapp/register.html")

