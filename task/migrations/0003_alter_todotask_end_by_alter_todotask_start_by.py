# Generated by Django 5.0.4 on 2024-04-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_todotask_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='end_by',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='todotask',
            name='start_by',
            field=models.TimeField(),
        ),
    ]
