from rest_framework import serializers

from .models.ingredient import Ingredient

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        #can put extra validations here
        model = Recipe
        fields = '__all__'
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        #can put extra validations here
        model = Ingredient
        fields = '__all__'
class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        #can put extra validations here
        model = RecipeIngredient
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        #can put extra validations here
        model = Comment
        fields = '__all__'
