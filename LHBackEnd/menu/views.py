from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError
)
from rest_framework.response import Response

from rest_framework.permissions import AllowAny

from .models import (
    Category, Recipe
)
from .serializers import (
    CategorySerializer, RecipeSerializer,
)

class CategoryViewSet(viewsets.ModelViewSet):
    
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        # list  categories 
        queryset = Category.objects.all()
        return queryset

    def get_object(self):
        if self.kwargs.get("pk"):
            category = Category.objects.filter(pk=self.kwargs.get("pk")).first()
            if not category:
                msg='Category with that id does not exists'
                raise ValidationError(msg)

        return category

    def create(self, request):
        # check if category already exists 
        category = Category.objects.filter(
            name=request.data.get('name'),
        )
        if category:
            msg='Category with that name already exists'
            raise ValidationError(msg)
        return super().create(request)
    
    def destroy(self, request, *args, **kwargs):
        category = Category.objects.filter(pk=self.kwargs["pk"]).first()
        if not category:
            msg='Category with that id does not exists'
            raise ValidationError(msg)

        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        category = Category.objects.filter(pk=self.kwargs["pk"]).first()
        if not category:
            msg='Category with that id does not exists'
            raise ValidationError(msg)

        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):            
        serializer.save()

class CategoryRecipes(generics.ListCreateAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = RecipeSerializer

    def get_queryset(self):
        if self.kwargs.get("category_pk"):
            category = Category.objects.filter(pk=self.kwargs["category_pk"]).first()
            if not category:
                msg='Category with that id does not exists'
                raise ValidationError(msg)

            queryset = Recipe.objects.filter(
                category=category
            )

        return queryset

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)

    #     if not serializer.is_valid():
    #         return Response(
    #             serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     category = Category.objects.get(pk=self.kwargs["category_pk"])

    #     item = Recipe.objects.create(
    #         name=serializer.data['name'],
    #         description=serializer.data['description'], 
    #         ingredients=serializer.data['ingredients'],
    #         image=serializer.data['image'],
    #         directions=serializer.data['directions'],
    #         is_public=serializer.data['is_public'],
    #         category=category,
    #         )

    #     result = self.serializer_class(item)
    #     return Response(result.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        category = Category.objects.filter(pk=self.kwargs["category_pk"]).first()
        if not category:
            msg='Category with that id does not exists'
            raise ValidationError(msg)

        serializer.save(category=category)

class SingleCategoryRecipe(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = RecipeSerializer
    
    def get_queryset(self):
        if self.kwargs.get("category_pk") and self.kwargs.get("pk"):
            category = Category.objects.filter(pk=self.kwargs["category_pk"]).first()
            if not category:
                msg='Category with that id does not exists'
                raise ValidationError(msg)

            queryset = Recipe.objects.filter(
                pk=self.kwargs["pk"],
                category=category
            )

            if len(queryset) == 0:
                msg=f'Recipe with that id does not exists'
                raise ValidationError(msg)

        return queryset

class RecipesViewSet(viewsets.ModelViewSet):
    
    permission_classes = (AllowAny,)
    serializer_class = RecipeSerializer
    
    def get_queryset(self):
        queryset = Recipe.objects.all()   
        return queryset

    # Only authenticated users can create recipes
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

class PublicRecipes(generics.ListAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = RecipeSerializer
    
    def get_queryset(self):
        queryset = Recipe.objects.all().filter(is_public=True)
        return queryset

class PublicRecipesDetail(generics.RetrieveAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = RecipeSerializer
    
    def get_queryset(self):
        queryset = Recipe.objects.all().filter(is_public=True)
        return queryset
