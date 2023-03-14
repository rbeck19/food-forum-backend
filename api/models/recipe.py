from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField



# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    ingredients = ArrayField(models.CharField(max_length=1000, blank=False))
    steps = ArrayField(models.CharField(max_length=2000, blank=False))
    image = models.CharField(null=True, blank=True, max_length=1000)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.description} {self.steps}'