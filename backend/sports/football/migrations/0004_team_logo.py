# Generated by Django 5.0.3 on 2024-03-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0003_alter_matchgame_options_matchgame_played'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]