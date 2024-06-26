# Generated by Django 5.0.4 on 2024-04-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('note', models.TextField()),
                ('start_by', models.DateTimeField()),
                ('end_by', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['start_by'],
            },
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
