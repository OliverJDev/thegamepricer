# Generated by Django 5.0.1 on 2024-06-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0007_remove_gameprice_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameprice',
            name='latest',
            field=models.BooleanField(default=True),
        ),
    ]