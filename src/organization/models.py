from datetime import date

from django.db import models


class Division(models.Model):
    class Meta:
        verbose_name = "подразделение"
        verbose_name_plural = "подразделения"

    name = models.CharField("наименование", max_length=60)
    head = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subordinates",
        verbose_name="головное подразделение",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"

    last_name = models.CharField("фамилия", max_length=60)
    first_name = models.CharField("имя", max_length=60)
    patronymic = models.CharField("отчество", max_length=60)
    age = models.SmallIntegerField("возраст")
    position = models.CharField("должность", max_length=60)
    date_of_employment = models.DateField("дата приема на работу", default=date.today)
    wage = models.IntegerField("заработная плата", default=0)
    division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name="подразделение",
    )

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def __str__(self):
        return self.full_name
