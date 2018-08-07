from django.db import models

from region.models import City, Country
from accommodations import crawlers


class PopularHotelInfo(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )

    def get_popularhotel_list(self):
        popularhotel_list = crawlers.PopularHotelList(
            city=self.city,
            country=self.country
        )
        popularhotel_list.search_popularhotel()
        result = popularhotel_list.popularhotel_list
        return result


class PopularHotel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )
    thumbnail = models.ImageField(upload_to='popularhotel', blank=True)
    comments = models.CharField(max_length=50, blank=True)
    price = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    # like = models.ForeignKey


class PopularHotelPriceInfo(models.Model):
    popular_hotel = models.ForeignKey(
        PopularHotel,
        on_delete=models.CASCADE,
        null=True,
    )
    date = models.IntegerField()
    price = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.popular_hotel}의 가격 : {self.price}'
