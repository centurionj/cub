# Generated by Django 4.2.6 on 2023-11-07 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
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
    ]
