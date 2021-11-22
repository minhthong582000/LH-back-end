from django.contrib import admin
from userprofile.models import Friend, Favorite, User
from menu.models import Recipe

# Register your models here.
admin.site.register(User)
admin.site.register(Friend)
admin.site.register(Favorite)