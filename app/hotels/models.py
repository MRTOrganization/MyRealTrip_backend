from django.db import models

from region.models import City


class KoreanHotel(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )
    thumbnail = models.ImageField('koreanhotel')
    comments = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
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


