# Generated by Django 4.2.6 on 2023-11-29 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_remove_task_comments_alter_taskcomment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 29, 13, 8, 14, 831879, tzinfo=datetime.timezone.utc), null=True, verbose_name='Дата'),
        ),
    ]
