# Generated by Django 4.2.5 on 2024-07-17 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-03-21'),
            preserve_default=False,
        ),
    ]
