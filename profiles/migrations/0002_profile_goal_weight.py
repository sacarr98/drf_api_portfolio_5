# Generated by Django 5.0.6 on 2024-06-02 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='goal_weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
