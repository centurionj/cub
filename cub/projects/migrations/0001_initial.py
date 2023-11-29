# Generated by Django 4.2.6 on 2023-11-29 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название папки')),
            ],
            options={
                'verbose_name': 'Папка',
                'verbose_name_plural': 'Папки',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала проекта')),
                ('stop_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения проекта')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_projects', to='customers.customerprofile', verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название файла')),
                ('file', models.FileField(upload_to='project_files/', verbose_name='Файл')),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to='projects.folder')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='projects.project')),
            ],
            options={
                'verbose_name': 'Файл проекта',
                'verbose_name_plural': 'Файлы проекта',
            },
        ),
    ]
