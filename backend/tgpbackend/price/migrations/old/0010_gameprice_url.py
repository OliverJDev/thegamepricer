# Generated by Django 5.0.1 on 2024-06-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0009_remove_gameprice_latest'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameprice',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]