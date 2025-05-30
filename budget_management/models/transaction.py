from django.db import models
from .category import Category, SubCategory
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from base import BaseModel


class Transaction(BaseModel):
    class ExpenceTypes(models.TextChoices):
        INCOME = "IN", _("Income")
        EXPENCE = "EX", _("Expense")

    amount = models.IntegerField()
    type = models.CharField(choices=ExpenceTypes)
    category = models.ForeignKey(
        to=Category, on_delete=models.SET_NULL
    )
    sub_category = models.ForeignKey(
        to=SubCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateField(db_index=True)
    note = models.TextField(max_length=500)

    def __str__(self):
        return self.note

    class Meta:
        ordering = ["created_at"]
