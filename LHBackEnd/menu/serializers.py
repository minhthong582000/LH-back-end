from rest_framework import serializers

from .models import (
    Category, Recipe
)

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id', 
            'name', 
            'description', 
            'ingredients', 
            'image',
            'directions',
            'is_public',
            'created_at', 
            'updated_at'
            )


class CategorySerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        fields = (
            'id', 
            'name', 
            'description', 
            'recipes',
            'created_at', 
            'updated_at'
            )