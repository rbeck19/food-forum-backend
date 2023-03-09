from django.urls import path
from .views.comment_view import IngredientsView, IngredientDetailView

# you must call your url pathing var this!
urlpatterns = [
    path('ingredients/', IngredientsView.as_view()),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view()),
]