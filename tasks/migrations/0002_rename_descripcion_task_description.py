# Generated by Django 4.1.6 on 2023-02-14 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descripcion',
            new_name='description',
        ),
    ]
