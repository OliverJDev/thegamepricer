# Generated by Django 5.0.1 on 2024-05-27 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0023_remove_game_artworks_game_artwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='screenshots',
        ),
        migrations.AddField(
            model_name='game',
            name='screenshot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screenshot', to='games.image'),
        ),
    ]
