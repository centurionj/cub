# Generated by Django 4.2.6 on 2023-11-25 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_alter_taskcomment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='comments',
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 25, 13, 31, 31, 49719, tzinfo=datetime.timezone.utc), null=True, verbose_name='Дата'),
        ),
    ]