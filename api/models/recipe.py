from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from .ingredient import Ingredient
from .recipeIng import RecipeIngredient
from .comment import Comment

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    ingredients = models.ManyToManyField(
        Ingredient,
        through = RecipeIngredient,
        through_fields = ('recipe','ingredients')
    )
    steps = ArrayField(models.CharField(max_length=500, blank=False))
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.description} {self.steps}'