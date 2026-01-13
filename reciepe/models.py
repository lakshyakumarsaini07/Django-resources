from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Receipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text="Minutes")
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

