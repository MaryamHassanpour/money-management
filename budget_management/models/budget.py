from django.db import models
from category import Category, SubCategory
from django.contrib.auth.models import User
from models.transaction import Transaction
from django.db.models import Sum
from base import BaseModel


class Budget(BaseModel):
    name = models.CharField(max_length=30)
    amount = models.IntegerField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(
        to=SubCategory, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name

    def get_remaining_amount_by_category(self, user, category) -> int:
        return (
            self.amount
            - Transaction.objects.filter(created_by=user, category=category).aggregate(
                total=Sum("amount")
            )["total"]
            or 0
        )

    def get_remaining_amount_by_sub_category(self, user, sub_category) -> int:
        return (
            self.amount
            - Transaction.objects.filter(
                created_by=user, sub_category=sub_category
            ).aggregate(total=Sum("amount"))["total"]
            or 0
        )
