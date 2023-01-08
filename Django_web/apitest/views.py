from django.shortcuts import render
from django.http import HttpRequest, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, "home.html")
