from django.db import models


STATUS_CHOICES = [
    ('pending', 'Ожидает выполнения'),
    ('in_progress', 'В процессе'),
    ('completed', 'Выполнено'),
]


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )

    def __str__(self):
        return self.title
