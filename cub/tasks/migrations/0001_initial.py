# Generated by Django 4.2.6 on 2023-11-05 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок задачи')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('status', models.CharField(choices=[('stopped', 'завершена'), ('paused', 'остановлена'), ('new', 'новая'), ('in_work', 'в работе')], default='new', max_length=50, verbose_name='Статус задачи')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='Срок выполнения задачи')),
                ('is_paused', models.BooleanField(default=False, verbose_name='На паузе')),
                ('is_stopped', models.BooleanField(default=False, verbose_name='Завершена')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Время выполнения задачи')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='Проект')),
            ],
        ),
    ]