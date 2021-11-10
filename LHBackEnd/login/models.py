from django.db import models
import datetime
class Role(models.Model):
    class Meta:
        verbose_name_plural = 'roles'
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class User(models.Model):
    role = models.ForeignKey(Role, related_name='users',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    birthday = models.DateTimeField(default=None)
    description = models.TextField(blank=True)
    image = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_age():
        return datetime.date.today().year - self.birthday.year