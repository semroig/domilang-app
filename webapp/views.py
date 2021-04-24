from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

class NewUserForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")
    rep_password = forms.CharField(label="Repet password")

class LogInForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")

def index(request):
    return render(request, "webapp/index.html")

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data["username"]
            new_password = form.cleaned_data["password"]
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "webapp/register.html", {
                "form": form
            })
    return render(request, "webapp/register.html", {
        "form": NewUserForm()
    })

def login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "webapp/login.html", {
                "form": form
            })
    return render(request, "webapp/login.html", {
        "form": LogInForm()
    })
    
def home(request):
    return render(request, "webapp/home.html")