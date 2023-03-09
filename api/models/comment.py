from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Comment(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    note = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.note} created by {self.owner}'