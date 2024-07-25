# Generated by Django 5.0.1 on 2024-05-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_alter_image_animated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='main_game_franchise',
        ),
        migrations.RemoveField(
            model_name='game',
            name='other_game_franchises',
        ),
        migrations.AddField(
            model_name='game',
            name='franchises',
            field=models.ManyToManyField(blank=True, related_name='franchises', to='games.gamefranchise'),
        ),
    ]