# Generated by Django 4.2.6 on 2023-11-29 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(limit_choices_to=models.Q(('role', 'programmer'), ('role', 'manager'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, related_name='executor_projects', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
        migrations.AddField(
            model_name='task',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='task_file', to='tasks.taskfile', verbose_name='Файлы к задаче'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='Проект'),
        ),
        migrations.AddField(
            model_name='task',
            name='project_manager',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(('role', 'admin'), ('role', 'manager'), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='managed_projects', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер проекта'),
        ),
    ]
