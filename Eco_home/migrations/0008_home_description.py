# Generated by Django 4.1.11 on 2024-02-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eco_home', '0007_alter_tourrequest_home_alter_tourrequest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='description',
            field=models.TextField(default='', max_length=2000),
        ),
    ]
