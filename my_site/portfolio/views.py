import os
from django import views
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.templatetags.static import static


main_menu = [
    {
        'title': 'About me',
        'url': 'about-me',
        'photo': 'oskar_in_air.jpg',
        'desc': 'Briefly about me'
    },
    {
        'title': 'My Curriculum',
        'url': 'my-cv',
        'photo': 'cv.png',
        'desc': 'Brief overview of my carrier'
    },
    {
        'title': 'My achievements',
        'url': 'achievements',
        'photo': 'achievements.jpg',
        'desc': 'Brief overview of my achievements'
    }
]

achievements = [
    {
        'slug': 'dci-page',
        'title': 'Digital Career Institute Python Course',
        'url': 'about-me',
        'logo': 'dci_logo1.png',
        'cert': 'work_in_progress.png',
        'desc': 'Bla Bla'
    },
    {
        'slug': 'python3',
        'title': 'Python Udemy Course',
        'url': 'about-me',
        'logo': 'python_logo.jpg',
        'cert': 'python3.png',
        'desc': 'Bla Bla'
    },
    {
        'slug': 'mysql',
        'title': 'MySQL Udemy Course',
        'url': 'about-me',
        'logo': 'mysql_logo.png',
        'cert': 'mysql.png',
        'desc': 'Bla Bla'
    },
    {
        'slug': 'github',
        'title': 'GitHub Udemy Course',
        'url': 'about-me',
        'logo': 'github_logo.png',
        'cert': 'github.png',
        'desc': 'Bla Bla'
    },
    {
        'slug': 'django-page',
        'title': 'Django Udemy Course',
        'url': 'about-me',
        'logo': 'django_logo.png',
        'cert': 'work_in_progress.png',
        'desc': 'Bla Bla'
    },
    {
        'slug': 'java',
        'title': 'Java Bootcamp',
        'url': 'about-me',
        'logo': 'java_logo.jpg',
        'cert': 'java.png',
        'desc': 'Bla Bla'
    },
]


def index(request):
    return render(request, 'portfolio/starting-page.html', {
        'main_menu': main_menu
    })


def about_me(request):
    return render(request, 'portfolio/about-me.html')


def my_cv(request):
    return render(request, "portfolio/my_cv.html")


def achievements_page(request):
    return render(request, "portfolio/achievements.html", {
        'achievements': achievements
    })


def detail_page(request, slug):
    identified_page = next(
        achiev for achiev in achievements if achiev['slug'] == slug)
    return render(request, 'portfolio/detail-page.html', {
        'achievement': identified_page
    })
