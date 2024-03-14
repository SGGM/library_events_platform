from django.db import models

from organizations.models import Organization


class Event(models.Model):
    title = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name="Название"
    )
    description = models.TextField(
        blank=True,
        null=False,
        verbose_name="Описание"
    )
    organizations = models.ManyToManyField(
        Organization,
        related_name="organizations"
    )
    image = models.ImageField(
        verbose_name="Изображение"
    )
    date = models.DateTimeField(
        blank=True,
        null=False,
        verbose_name="Дата проведения"
    )
    created = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ["date"]

    def __str__(self):
        return f"{self.title}"
