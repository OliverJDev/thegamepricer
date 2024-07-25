# Generated by Django 5.0.1 on 2024-05-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_remove_game_main_game_franchise_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='main_collection',
        ),
        migrations.RemoveField(
            model_name='game',
            name='other_collections',
        ),
        migrations.AddField(
            model_name='game',
            name='collections',
            field=models.ManyToManyField(blank=True, related_name='collections', to='games.collection'),
        ),
    ]