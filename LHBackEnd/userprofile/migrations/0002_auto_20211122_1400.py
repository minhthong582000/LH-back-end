# Generated by Django 3.2.8 on 2021-11-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='credit',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('G', 'Gold'), ('S', 'Silver'), ('B', 'Bronze'), ('N', 'None')], default='N', max_length=2),
        ),
    ]
