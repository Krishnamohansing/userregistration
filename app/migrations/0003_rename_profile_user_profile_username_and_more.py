# Generated by Django 5.0.3 on 2024-06-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_username_profile_profile_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_user',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
