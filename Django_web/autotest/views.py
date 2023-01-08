from django.shortcuts import render
from django.http import HttpRequest, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login


def login(requset):
    if requset.POST:
        passwoord = username = ""
        username = requset.POST.get("username")
        passwoord = requset.POST.get("password")
        user = auth.authenticate(username=username, passwoord=passwoord)
        if user is not None and user.is_active:
            auth.login(requset, user)
            requset.session["user"] = username
            response = HttpResponseBadRequest("/home/")
            return response
        else:
            return render(requset, "login.html", {"error": "username or password error"})
    return render(requset, "login.html")
def home(request):
    return  render(request,"home.html")