from django.db import models


# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=10, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)


class CurrencyRate(models.Model):
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name="rates",
    )
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    creates_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]