# Generated by Django 5.0.6 on 2024-06-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
