from django.db import models
from products.models import TicketInfo, GuideTourInfo
from members.models import User
from hotels.models import KoreanHotel


class Wishlist(models.Model):
    ticket = models.ManyToManyField(
        TicketInfo,
        related_name=''
    )

    guide = models.ManyToManyField(
        GuideTourInfo,
        related_name=''
    )
    user = models.ManyToManyField(
        User,
        related_name=''
    )

    korean_hotel = models.ManyToManyField(
        KoreanHotel,
        related_name=''
    )
