from django.urls import path
from .views.comment_view import CommentsView, CommentDetailView
from .views.ingredient_view import IngredientsView, IngredientDetailView
from .views.recipe_view import RecipesView, RecipeDetailView
from .views.recipeIng_view import RecipeIngredientsView, RecipeIngredientDetailView

# you must call your url pathing var this!
urlpatterns = [
    path('ingredients/', IngredientsView.as_view()),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view()),
    path('recipes/', RecipesView.as_view()),
    path('recipes/<int:pk>/', RecipeDetailView.as_view()),
    path('comment/', CommentsView.as_view()),
    path('comment/<int:pk>/', CommentDetailView.as_view()),
    path('recipeIng/', RecipeIngredientsView.as_view()),
    path('recipeIng/<int:pk>/', RecipeIngredientDetailView.as_view())
]