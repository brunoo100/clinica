# Generated by Django 5.1.2 on 2024-10-27 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_consulta_data_hora_consulta_data_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='user',
        ),
    ]
