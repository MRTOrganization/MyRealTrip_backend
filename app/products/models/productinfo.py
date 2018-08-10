from django.conf import settings
from django.db import models

from products import crawler
from region.models import City, Country


class ProductList(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )
    tour_name = models.CharField(max_length=15)
    thumbnail = models.ImageField(upload_to='product_thumbnail', blank=True)
    title = models.CharField(max_length=100)
    review = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    meta_info = models.CharField(max_length=20, blank=True)

    def get_product_list_crawler(self):
        product_list = crawler.ProductList(
            city=self.city,
            country=self.country,
            tour_name=self.tour_name,
            thumbnail=self.thumbnail,
            title=self.title,
            review=self.review,
            price=self.price,
            category=self.category,
            meta_info=self.meta_info
        )
        product_list.get_product_list()
        result = product_list.get_product_list
        return result


class ProductDetailBase(models.Model):
    title = models.CharField(max_length=100)
    review_number = models.CharField(max_length=15, blank=True)
    product_type_icon = models.ImageField(upload_to='icon', blank=True)
    product_type_text = models.CharField(max_length=50, blank=True)
    date = models.IntegerField()
    photo_review = models.ImageField(upload_to='review', blank=True)
    text_review = models.TextField(blank=True)
    guide_name = models.CharField(max_length=20)
    guide_description = models.TextField()
    necessary_guide = models.TextField(blank=True)

    class Meta:
        abstract = True


class ProductTicketDetail(ProductDetailBase):
    region = models.ManyToManyField(
        City,
        related_name='city_ticket',
    )
    select_option = models.CharField(max_length=30)
    info_photo = models.ImageField(upload_to='information', blank=True)
    information = models.TextField()


class ProductGuideTourDetail(ProductDetailBase):
    region = models.ManyToManyField(
        City,
        related_name='city_guide',
    )
    tour_terms = models.TextField()
    course_image = models.ImageField(upload_to='course_image', blank=True)
    course_text = models.TextField(blank=True)


class ProductActivityDetail(ProductDetailBase):
    region = models.ManyToManyField(
        City,
        related_name='city_activity',
    )
    course_image = models.ImageField(upload_to='course_image', blank=True)
    course_text = models.TextField(blank=True)


class Comment(models.Model):
    ticket = models.ForeignKey(
        ProductTicketDetail,
        on_delete=models.CASCADE,
        null=True,
        related_name='comments_by_tickets',
    )
    guide = models.ForeignKey(
        ProductGuideTourDetail,
        on_delete=models.CASCADE,
        null=True,
        related_name='comments_by_guide_tour',
    )
    activity = models.ForeignKey(
        ProductActivityDetail,
        on_delete=models.CASCADE,
        null=True,
        related_name='comments_by_activity',
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

    class Meta:
        abstract = True


# class TicketPriceInfo(PriceInfoBase):
#     ticket = models.ForeignKey(
#         TicketInfo,
#         on_delete=models.CASCADE,
#         null=True,
#         related_name='ticket_price',
#     )
#
#     def __str__(self):
#         return f'{self.ticket}의 가격 : {self.price}'
#
#
# class GuidePriceInfo(PriceInfoBase):
#     guide = models.ForeignKey(
#         GuideTourInfo,
#         on_delete=models.CASCADE,
#         null=True,
#         related_name='guide_price',
#     )
#
#     def __str__(self):
#         return f'{self.guide}의 가격 : {self.price}'
#
#
# class ActivityPriceInfo(PriceInfoBase):
#     activity = models.ForeignKey(
#         ActivityInfo,
#         on_delete=models.CASCADE,
#         null=True,
#         related_name='activity_price',
#     )
#
#     def __str__(self):
#         return f'{self.activity}의 가격 : {self.price}'
