from django.db import models
from .ingredient import Ingredient


# Create your models here.
class RecipeIngredient(models.Model):
    amount = models.IntegerField()
    unit = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE
    )
    ingredients = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.amount} {self.unit}"
