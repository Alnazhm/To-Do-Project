from django.db import models

STATUS_OF_TASK = [
    ('New', 'Новая'),
    ('In Progress', 'В работе'),
    ('Completed', 'Завершена')
]

class Todo(models.Model):
    description = models.CharField(verbose_name="Описание", max_length=200, null=False, blank=False)
    status = models.CharField(verbose_name="Статус", choices=STATUS_OF_TASK, max_length=50, null=False, blank=False)
    lead_at = models.DateField(verbose_name="Время выполнения")
    detail_description = models.TextField(verbose_name="Детальное описание", default="")


    def __str__(self):
        return f"{self.description} - {self.status}"

