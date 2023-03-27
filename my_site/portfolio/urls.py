from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("about-me", views.about_me, name="about-me"),
    path("cv", views.my_cv, name="my-cv"),
    path("achievements", views.achievements, name="achievements"),
    path("achievements/java", views.java, name="java"),
    path("achievements/python3", views.python3, name="python3"),
    path("achievements/mysql", views.sql_page, name="mysql"),
    path("achievements/github", views.github_page, name="github"),
    path("achievements/django-cert", views.django_page, name="django-page"),
    path("achievements/dci", views.dci_page, name="dci-page"),
]
