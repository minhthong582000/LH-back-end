from django.urls import path, include
from knox.views import LogoutView
from userprofile.views import UserDetail
from .views import RegisterDetail, LoginDetail

urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserDetail.as_view()),
    path('register', RegisterDetail.as_view()),
    path('login', LoginDetail.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout')
]