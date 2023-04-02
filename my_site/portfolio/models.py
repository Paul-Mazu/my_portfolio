from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    photo_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    logo_name = models.CharField(max_length=50)
    certificate_name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.title