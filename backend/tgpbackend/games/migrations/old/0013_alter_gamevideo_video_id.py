# Generated by Django 5.0.1 on 2024-05-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0012_remove_collection_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamevideo',
            name='video_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]