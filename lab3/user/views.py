from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
from .forms import loginForm , SignUpForm

# Create your views here.

def user_login(request):
    form = loginForm()
    if request.user.is_authenticated:
        return redirect("BookStore_index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "Pages/logIn.htm", {"form": form})
        login(request , user)
        return redirect("BookStore_index")
    else:
        return render(request, "Pages/logIn.html" , {"form": form})

def user_logout(request):
    logout(request)
    return redirect("user:login")


def user_signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("user:login")
        else:
           errors = form.errors
           return render(request, "Pages/register.html" , {"form": form },{'errors':errors})
    else:
        return render(request, "Pages/register.html" , {"form": form})
