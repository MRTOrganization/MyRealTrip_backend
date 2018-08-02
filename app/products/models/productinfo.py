from django.conf import settings
from django.db import models
from region.models import City


class ProductBase(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    date = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class TicketInfo(ProductBase):
    region = models.ManyToManyField(
        City,
        related_name='city_ticket',
    )


class GuideTourInfo(ProductBase):
    name = models.CharField(max_length=5)
    region = models.ManyToManyField(
        City,
        related_name='city_guide',
    )


class ActivityInfo(ProductBase):
    region = models.ManyToManyField(
        City,
        related_name='city_activity',
    )


class Comment(models.Model):
    ticket = models.ForeignKey(
        TicketInfo,
        on_delete=models.CASCADE,
        null=True,
        related_name='comments_by_tickets',
    )
    guide = models.ForeignKey(
        GuideTourInfo,
        on_delete=models.CASCADE,
        null=True,
        related_name='comments_by_guide_tour',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author.username}님의 댓글(후기)'


class PriceInfoBase(models.Model):
    date = models.IntegerField()
    price = models.CharField(max_length=100, blank=True)


class TicketPriceInfo(PriceInfoBase):
    ticket = models.ForeignKey(
        TicketInfo,
        on_delete=models.CASCADE,
        null=True,
        related_name='ticket_price',
    )

    def __str__(self):
        return f'{self.ticket}의 가격 : {self.price}'


class GuidePriceInfo(PriceInfoBase):
    guide = models.ForeignKey(
        GuideTourInfo,
        on_delete=models.CASCADE,
        null=True,
        related_name='guide_price',
    )

    def __str__(self):
        return f'{self.guide}의 가격 : {self.price}'


class ActivityPriceInfo(PriceInfoBase):
    activity = models.ForeignKey(
        ActivityInfo,
        on_delete=models.CASCADE,
        null=True,
        related_name='activity_price',
    )

    def __str__(self):
        return f'{self.activity}의 가격 : {self.price}'
