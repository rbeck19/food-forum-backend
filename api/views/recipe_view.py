from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response

from ..models.recipe import Recipe
from ..serializers import RecipeSerializer

class RecipesView(generics.ListCreateAPIView):
    """
    View Recipes
    """
    serializer_class = RecipeSerializer
    #INDEX
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response({'recipes': serializer.data})
    #CREATE
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /recipes/id
class RecipeDetailView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    #UPDATE
    def patch(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    def delete(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)