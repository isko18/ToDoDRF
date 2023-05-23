# Generated by Django 4.2 on 2023-05-19 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Описание')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('image', models.ImageField(upload_to='todo_images/', verbose_name='Фотография')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_todo', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Таск',
                'verbose_name_plural': 'Таски',
            },
        ),
    ]
