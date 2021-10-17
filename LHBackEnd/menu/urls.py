from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet, CategoryRecipes,
    SingleCategoryRecipe, PublicRecipes,
    PublicRecipesDetail
)

app_name = 'menu_app'

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')

custom_urlpatterns = [
    url(r'categories/(?P<category_pk>\d+)/recipes$',
        CategoryRecipes.as_view(), name='category_recipes'),
    url(r'categories/(?P<category_pk>\d+)/recipes/(?P<pk>\d+)$',
        SingleCategoryRecipe.as_view(), name='single_category_recipe'),
    url(r'public-recipes/$', PublicRecipes.as_view(), name='public_recipes'),
    url(r'public-recipes/(?P<pk>\d+)/$', PublicRecipesDetail.as_view(),
        name='public_recipes_detail'),
]

urlpatterns = router.urls

urlpatterns += custom_urlpatterns
