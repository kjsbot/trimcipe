from django.conf.urls import handler404
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("recipe", views.recipe, name="recipe"),
    path("shelf", views.shelf, name="shelf"),
    path("login_view", views.login_view, name="login_view"),
    path("logout_view", views.logout_view, name="logout_view"),
    path("register", views.register, name="register")
]