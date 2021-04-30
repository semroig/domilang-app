from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

class LogInForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")

def index(request):
    if not request.user.is_authenticated:
        return render(request, "webapp/index.html")
    return render(request, "webapp/index.html", {
        "message": "You are logged in! Start paying please."
    })

def login_view(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("webapp:index"))
            else:
                return render(request, "webapp/login.html", {
                    "message": "Invalid credentials."
                })
        else:
            return render(request, "webapp/login.html", {
                "form": form
            })
    return render(request, "webapp/login.html", {
        "form": LogInForm()
    })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("webapp:index"))