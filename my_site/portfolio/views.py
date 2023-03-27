import os
from django import views
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.templatetags.static import static


# cards = [
#     {
#     'slug':''
#     }
# ]


def index(request):
    return render(request, 'portfolio/starting-page.html')

def about_me(request):
    return render(request, 'portfolio/about-me.html')

def my_cv(request):
    return render(request, "portfolio/my_cv.html")

def achievements(request):
    return render(request, "portfolio/achievements.html")

def java(request):
    return render(request, "portfolio/java.html")

def python3(request):
    return render(request, "portfolio/python3.html")

def sql_page(request):
    return render(request, "portfolio/sql.html")

def github_page(request):
    return render(request, "portfolio/github.html")

def django_page(request):
    return render(request, "portfolio/django-page.html")

def dci_page(request):
    return render(request, "portfolio/dci-page.html")


