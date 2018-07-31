from django.db import models
from members.models import User
from hotels.models import KoreanHotel
from products.models.productinfo import TicketInfo, GuideTourInfo


class Wishlist(models.Model):
    ticket = models.ManyToManyField(
        TicketInfo,
        related_name='ticket_wishlist'
    )
    guide = models.ManyToManyField(
        GuideTourInfo,
        related_name='guide_wishlist'
    )
    korean_hotel = models.ManyToManyField(
        KoreanHotel,
        related_name='korean_hotel_wishlist'
    )
    member = models.ManyToManyField(
        User,
        related_name='wishlist_of_member'
    )

