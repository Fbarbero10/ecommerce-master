# Generated by Django 4.0.5 on 2022-06-24 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ComercioApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='nombre',
        ),
    ]
