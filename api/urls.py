from django.urls import path
from .views.comment_view import CommentsView, CommentDetailView
from .views.recipe_view import RecipesView, RecipeDetailView
from .views.user_view import SignUp, SignIn, SignOut

# you must call your url pathing var this!
urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('recipes/', RecipesView.as_view()),
    path('recipes/<int:pk>/', RecipeDetailView.as_view()),
    path('comment/', CommentsView.as_view()),
    path('comment/<int:pk>/', CommentDetailView.as_view()),
]