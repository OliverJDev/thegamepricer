# Generated by Django 5.0.1 on 2024-05-21 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_alter_game_category_alter_game_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='collection',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='gameengine',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='gameengine',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='gamefranchise',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='gamefranchise',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='gamegenre',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='gamegenre',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='gamekeyword',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='gamekeyword',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='gamemodes',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='gamemodes',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='gametheme',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='gametheme',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='gamevideo',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='platform',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='platform',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='platform',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='playerperspective',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='playerperspective',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]