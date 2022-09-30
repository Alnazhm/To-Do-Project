from datetime import timezone

from django.db import models
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    NEW = 'New', 'New'
    IN_PROGRESS = 'In Progress', 'In Progress'
    COMPLETED = 'Completed', 'Completed'


class Todo(models.Model):
    description = models.CharField(verbose_name="Описание", max_length=200, null=False, blank=False)
    status = models.CharField(verbose_name="Статус", choices=StatusChoices.choices, default=StatusChoices.NEW, max_length=50, null=False, blank=False)
    lead_at = models.DateField(verbose_name="Время выполнения")
    detail_description = models.TextField(verbose_name="Детальное описание", default="")
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)


    def __str__(self):
        return f"{self.description} - {self.status}"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
