from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'userprofile'

urlpatterns = [
    path('profile/<int:pk>/', views.OtherUserDetail.as_view()), #includes favorites, and friends' recipes for the feed
    path('profile/<int:pk>/favorites/', views.UserFavoriteList.as_view()),
    path('profile/<int:pk>/friends/', views. UserFriendsList.as_view()),
    path('profile/search/<str:query>/', views. UserSearchList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)