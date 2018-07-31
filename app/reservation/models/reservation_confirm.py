from django.conf import settings
from django.db import models

from products.models.product_confirm import ProductSchedule


class ReservationConfirm(models.Model):
    travel_schedule = models.ForeignKey(
        ProductSchedule,
        on_delete=models.CASCADE,
    )
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    travel_date = models.CharField(max_length=20)
    reservation_number = models.CharField(max_length=10)

    def total_price(self):
        pass
