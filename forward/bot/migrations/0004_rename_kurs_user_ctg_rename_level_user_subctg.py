# Generated by Django 4.0.6 on 2023-03-16 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_rename_name_en_subctg_name_remove_subctg_name_ru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='kurs',
            new_name='ctg',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='level',
            new_name='subctg',
        ),
    ]