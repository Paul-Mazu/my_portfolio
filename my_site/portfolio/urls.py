from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("about-me", views.about_me, name="about-me"),
    path("cv", views.my_cv, name="my-cv"),
    path("achievements", views.achievements_page, name="achievements"),
    path("achievements/<slug:slug>", views.detail_page, name="achievements-detail-page"),
]
