from django.conf import settings
from django.db import models
from menu.models import Recipe
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class UserType(models.TextChoices):
        GOLD = 'G', _('Gold')
        SILVER = 'S', _('Silver')
        BRONZE = 'B', _('Bronze')
        NONE = 'N', _('None')

    user_type = models.CharField(
        max_length=2,
        choices=UserType.choices,
        default=UserType.NONE,
    )
    is_teacher = models.BooleanField(default=False)
    email = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=140, blank=True)
    about_me = models.TextField(blank=True)
    credit = models.FloatField(blank=False, default=0)

class Favorite(models.Model):
    user = models.OneToOneField(User, related_name='favorites', on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Recipe)
    def __str__(self):
        return "%s's favorites" % self.user

class Friend(models.Model):
    users = models.ManyToManyField(User, related_name='users')
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s's friends" % self.current_user

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)