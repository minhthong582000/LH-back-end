from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    category = models.ForeignKey(Category, related_name='recipes',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calo = models.FloatField(blank=True, default=0)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    directions = models.TextField()
    image = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name
