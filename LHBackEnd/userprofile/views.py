from django.contrib.auth.decorators import login_required
from .models import User
from django.db.models.functions import Lower
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.exceptions import (
    ValidationError
)

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from menu.models import Recipe
from menu.serializers import RecipeSerializer
from userprofile.models import Friend, Favorite
from .serializers import UserSerializer, OtherUserSerializer, FriendSerializer, UserFavoritesSerializer, UserSearchSerializer

import json


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer
    def get_object(self):
        if self.request.user.id == None:
            return self.request.user.id
        return self.request.user

class OtherUserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = OtherUserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserFavoriteList(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    all_favorites = Favorite.objects.all()
    
    def get_queryset(self):
        user = User.objects.get(id=self.kwargs['pk'])
        favorites_obj = get_object_or_404(self.all_favorites, user=user)
        return favorites_obj.favorites.all()
        
    def post(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            favorites_obj = get_object_or_404(self.all_favorites, user=user)
            if "recipe_id" not in request.data:
                msg='Please provide recipe_id'
                raise ValidationError(msg)
            recipe = Recipe.objects.get(id=request.data['recipe_id'])
            if favorites_obj:
                favorites_obj.favorites.add(recipe)
            return Response(json.dumps({}))
        except User.DoesNotExist:
            msg='User with that id does not exists'
            raise ValidationError(msg)
        except Recipe.DoesNotExist:
            msg='Recipe with that id does not exists'
            raise ValidationError(msg)
    
    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        favorites_obj = get_object_or_404(self.all_favorites, user=user)
        recipe = Recipe.objects.get(id=request.data['recipe_id'])
        if favorites_obj:
            favorites_obj.favorites.remove(recipe)
        return Response(json.dumps({}))

class UserFriendsList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    all_users = Friend.objects.all()

    def get_queryset(self):
        user = User.objects.get(id=self.kwargs['pk'])
        friends_obj = Friend.objects.get_or_create(current_user=user)
        print(friends_obj)
        return friends_obj[0].users.all()
    
    def post(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            friends_obj = Friend.objects.get_or_create(current_user=user)[0]
            friend = User.objects.get(id=request.data['other_user_id'])
            if friends_obj:
                friends_obj.users.add(friend)
            return Response(json.dumps({}))
        except User.DoesNotExist:
            msg='User with that id does not exists'
            raise ValidationError(msg)
    
    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        friends_obj = Friend.objects.get_or_create(current_user=user)[0]
        friend = User.objects.get(id=request.data['other_user_id'])
        if friends_obj:
            friends_obj.users.remove(friend)
        return Response(json.dumps({}))

class UserSearchList(generics.ListAPIView):
    serializer_class = UserSearchSerializer
    
    def get_queryset(self):
        query = self.kwargs['query']

        if query == "all":
            queryset = User.objects.all()
        else:
            queryset = User.objects.filter(username__contains=query)
        return queryset