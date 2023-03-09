from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response

from ..models.ingredient import Ingredient
from ..serializers import IngredientSerializer

class IngredientsView(generics.ListCreateAPIView):
    """
    View Ingredients
    """
    serializer_class = IngredientSerializer
    #INDEX
    def get(self, request):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response({'ingredients': serializer.data})
    #CREATE
    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /ingredients/id
class IngredientDetailView(generics.ListCreateAPIView):
    serializer_class = IngredientSerializer
    
    def get(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)
    #UPDATE
    def patch(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    def delete(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)