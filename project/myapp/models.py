from django.db import models


# create your models here
class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default="null")
    published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()


class Motorcycle(models.Model):
    brand = models.CharField(max_length=50)
    reference = models.CharField(max_length=80)
