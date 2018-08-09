from django.db import models

from region.models import City, Country
from hotels import crawler


class KoreanHotelInfo(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )

    def get_koreanhotel_list(self):
        koreanhotel_list = crawler.KoreanHotelList(
            city=self.city,
            country=self.country
        )
        koreanhotel_list.search_koreanhotel()
        result = koreanhotel_list.koreanhotel_list
        return result


class KoreanHotel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )
    thumbnail = models.ImageField(upload_to='koreanhotel', blank=True)
    comments = models.CharField(max_length=50, blank=True)
    price = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    # like = models.ForeignKey


class KoreanHotelPriceInfo(models.Model):
    korean_hotel = models.ForeignKey(
        KoreanHotel,
        on_delete=models.CASCADE,
        null=True,
    )
    date = models.IntegerField()
    price = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.korean_hotel}의 가격 : {self.price}'
