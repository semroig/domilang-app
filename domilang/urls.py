from django.urls import path
from . import views

app_name = "domilang"
urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("home", views.home, name="home"),
    path("logout", views.logout_view, name="logout"),
    path("profile", views.profile, name="profile"),
    path("edit", views.edit, name="edit")
]