# Generated by Django 4.2.9 on 2024-01-09 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('pending', 'Ожидает выполнения'), ('in_progress', 'В процессе'), ('completed', 'Выполнено')], default='pending', max_length=20, verbose_name='Статус')),
            ],
        ),
    ]
