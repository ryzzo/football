# Generated by Django 5.0.3 on 2024-03-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0005_alter_stat_options_stat_goal_difference_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='goals_against',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stat',
            name='goals_for',
            field=models.PositiveIntegerField(default=0),
        ),
    ]