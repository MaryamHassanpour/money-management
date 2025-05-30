from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name="سازنده"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ساخت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="زمان تغییر")

    def __str__(self):
        return self.username
