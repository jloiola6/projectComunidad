# Generated by Django 3.1.2 on 2020-10-17 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_joao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='CPF',
        ),
    ]
