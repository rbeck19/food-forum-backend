from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response

from ..models.recipeIng import RecipeIng
from ..serializers import RecipeIngSerializer

class RecipeIngsView(generics.ListCreateAPIView):
    """
    View RecipeIngs
    """
    serializer_class = RecipeIngSerializer
    #INDEX
    def get(self, request):
        recipeings = RecipeIng.objects.all()
        serializer = RecipeIngSerializer(recipeings, many=True)
        return Response({'recipe_ingredients': serializer.data})
    #CREATE
    def post(self, request):
        serializer = RecipeIngSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /recipeings/id
class RecipeIngDetailView(generics.ListCreateAPIView):
    serializer_class = RecipeIngSerializer
    
    def get(self, request, pk):
        recipeing = get_object_or_404(RecipeIng, pk=pk)
        serializer = RecipeIngSerializer(recipeing)
        return Response(serializer.data)
    #UPDATE
    def patch(self, request, pk):
        recipeing = get_object_or_404(RecipeIng, pk=pk)
        serializer = RecipeIngSerializer(recipeing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    def delete(self, request, pk):
        recipeing = get_object_or_404(RecipeIng, pk=pk)
        recipeing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)