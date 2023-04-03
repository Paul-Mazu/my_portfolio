from django import views
from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static
from .models import Post, Achievement


def index(request):
    posts = Post.objects.all()
    return render(request, 'portfolio/starting-page.html', {
        'posts': posts
    })


def about_me(request):
    return render(request, 'portfolio/about-me.html')


def my_cv(request):
    return render(request, "portfolio/my_cv.html")


def achievements_page(request):
    achievements = Achievement.objects.all().order_by("-date")
    return render(request, "portfolio/achievements.html", {
        'achievements': achievements
    })


def detail_page(request, slug):
    identified_page = get_object_or_404(Achievement, slug=slug)
    return render(request, 'portfolio/detail-page.html', {
        'achievement': identified_page
    })
