# Generated by Django 4.2 on 2023-04-29 18:30

from django.db import migrations
import iniciar_sesion.models


class Migration(migrations.Migration):

    dependencies = [
        ('iniciar_sesion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', iniciar_sesion.models.CustomUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
