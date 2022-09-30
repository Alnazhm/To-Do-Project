# Generated by Django 4.1.1 on 2022-09-30 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_options_todo_deleted_at_todo_is_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='New', max_length=50, verbose_name='Статус'),
        ),
    ]
