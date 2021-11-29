# Generated by Django 3.2.8 on 2021-11-29 14:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercise', '0004_courses_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='Members', to=settings.AUTH_USER_MODEL),
        ),
    ]