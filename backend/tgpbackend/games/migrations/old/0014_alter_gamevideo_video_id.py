# Generated by Django 5.0.1 on 2024-05-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0013_alter_gamevideo_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamevideo',
            name='video_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]