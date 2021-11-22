from rest_framework import serializers
from django.core import serializers as dj_serializers
from .models import User
from django.db.models.functions import Lower

from . import views
from .models import Friend, Favorite

from menu.models import Recipe
from menu.serializers import RecipeSerializer


class UserSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'friends',
            'favorites',
            'is_teacher',
            'email',
            'name',
            'gender',
            'about_me',
            'user_type',
            'credit',
            ]

    def get_friends(self, obj):
        try:
            friend = Friend.objects.get(current_user=obj)
            friends = friend.users.all()
        except:
            friends = None
            return []
        friends_serializer = FriendSerializer(friends, many=True)
        return friends_serializer.data

    def get_favorites(self, obj):
        user_favorites, created = Favorite.objects.get_or_create(user=obj)
        favorite_recipes = obj.favorites.favorites.all()
        recipe_serializer = RecipeSerializer(favorite_recipes, many=True)
        return recipe_serializer.data

class OtherUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'name',
            'email',
            'gender',
            'is_teacher',
            'about_me',
            'user_type',
            'credit',
            ]

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class UserFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'