from django.db import models

from django.db import models
from userprofile.models import User
from menu.models import Recipe
from django.utils.translation import ugettext as _

class Schedule(models.Model):
    recipe = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    date = models.DateField()

    class Meta:
        managed = True

# We can now start discussion on it, that what we need to add more here.
# It is just a prototype
class Courses(models.Model):
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    description = models.TextField()
    teacher = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(User, related_name=_('Members'), null=True, blank=True)
    start_date = models.DateField()
    cost = models.FloatField(default=0)
    end_date = models.DateField()
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title