# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from rest_framework import status, generics
# from rest_framework.response import Response

# from ..models.recipeIng import RecipeIngredient
# from ..serializers import RecipeIngredientSerializer

# class RecipeIngredientsView(generics.ListCreateAPIView):
#     """
#     View RecipeIngs
#     """
#     serializer_class = RecipeIngredientSerializer
#     #INDEX
#     def get(self, request):
#         recipes = RecipeIngredient.objects.all()
#         serializer = RecipeIngredientSerializer(recipes, many=True)
#         return Response({'recipe_ingredients': serializer.data})
#     #CREATE
#     def post(self, request):
#         serializer = RecipeIngredientSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # /recipeings/id
# class RecipeIngredientDetailView(generics.ListCreateAPIView):
#     serializer_class = RecipeIngredientSerializer
    
#     def get(self, request, pk):
#         recipes = get_object_or_404(RecipeIngredient, pk=pk)
#         serializer = RecipeIngredientSerializer(recipes)
#         return Response(serializer.data)
#     #UPDATE
#     def patch(self, request, pk):
#         recipes = get_object_or_404(RecipeIngredient, pk=pk)
#         serializer = RecipeIngredientSerializer(recipes, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #DELETE
#     def delete(self, request, pk):
#         recipes = get_object_or_404(RecipeIngredient, pk=pk)
#         recipes.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)