# Generated by Django 4.1.11 on 2024-02-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eco_app', '0003_customercontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='unknown', max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='user', max_length=150),
        ),
    ]