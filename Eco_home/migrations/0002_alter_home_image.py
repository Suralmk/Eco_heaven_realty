# Generated by Django 4.1.11 on 2023-12-28 20:27

import Eco_home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eco_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(upload_to=Eco_home.models.home_directory_path),
        ),
    ]
