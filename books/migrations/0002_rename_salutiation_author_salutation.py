# Generated by Django 4.2.4 on 2023-12-20 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='salutiation',
            new_name='salutation',
        ),
    ]