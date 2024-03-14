from django.db import models

from users.models import User


class Organization(models.Model):
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
    address = models.CharField(
        max_length=256,
        blank=True,
        null=False,
        verbose_name= "Адрес"
    )
    postcode = models.CharField(
        max_length=16,
        blank=True,
        null=False,
        verbose_name="Почтовый индекс"
    )
    employees = models.ManyToManyField(
        User,
        related_name="employees"
    )

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return f"{self.title}"
