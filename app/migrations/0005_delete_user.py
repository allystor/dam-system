# Generated by Django 4.1.3 on 2023-06-17 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user_delete_userautentication'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
