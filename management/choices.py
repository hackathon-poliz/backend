from django.db import models


class RoleChoice(models.IntegerChoices):
    FARMER = 1, "Фермер"
    PROVIDER = 2, "Поставщик"
    WORKER = 3, "Сотрудники"