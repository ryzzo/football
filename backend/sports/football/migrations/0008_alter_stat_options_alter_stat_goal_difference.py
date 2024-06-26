# Generated by Django 5.0.3 on 2024-03-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0007_alter_stat_options_stat_points'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stat',
            options={'ordering': ['-points', 'team']},
        ),
        migrations.AlterField(
            model_name='stat',
            name='goal_difference',
            field=models.IntegerField(default=0),
        ),
    ]
