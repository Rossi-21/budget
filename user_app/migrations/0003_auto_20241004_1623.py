# Generated by Django 2.2.4 on 2024-10-04 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_auto_20241002_1442'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='catagory',
            new_name='category',
        ),
    ]
