# Generated by Django 4.1.1 on 2022-09-16 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topico',
            old_name='Autor',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='topico',
            old_name='Titulo',
            new_name='titulo',
        ),
    ]
