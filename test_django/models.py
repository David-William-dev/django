from typing import Any
from django.db import models
from django.utils.text import slugify


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class AboutPage(models.Model):
    content = models.TextField()

class ContactData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
        
    def __str__(self):
        return self.name
