from django.conf import settings
from django.db import models
from members.models import User
from hotels.models import KoreanHotel
from products.models.productinfo import ProductTicketDetail, ProductGuideTourDetail, ProductActivityDetail, Product


class WishList(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    product = models.ManyToManyField(
        Product,
    )
    # ticket = models.ManyToManyField(
    #     ProductTicketDetail,
    #     related_name='ticket_wishlist'
    # )
    # guide = models.ManyToManyField(
    #     ProductGuideTourDetail,
    #     related_name='guide_wishlist'
    # )
    # activity = models.ManyToManyField(
    #     ProductActivityDetail,
    #     related_name='activity_wishlist'
    # )
    # korean_hotel = models.ManyToManyField(
    #     KoreanHotel,
    #     related_name='korean_hotel_wishlist'
    # )
    # member = models.ManyToManyField(
    #     User,
    #     related_name='wishlist_of_member'
    # )

