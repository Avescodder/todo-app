from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Task model for storing user tasks
    """
    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    completed = models.BooleanField(default=False, verbose_name='Выполнено')
    priority = models.CharField(
        max_length=10, 
        choices=PRIORITY_CHOICES, 
        default='medium',
        verbose_name='Приоритет'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='tasks',
        verbose_name='Пользователь'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f"{self.title} - {self.user.username}"