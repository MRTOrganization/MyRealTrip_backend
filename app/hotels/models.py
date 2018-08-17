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

    def create_koreanhotel(self):
        koreanhotel_list = self.get_koreanhotel_list()
        for koreanhotel in koreanhotel_list:
            KoreanHotel.objects.create(
                name=koreanhotel.name,
                city=koreanhotel.city,
                country=koreanhotel.country,
                thumbnail=koreanhotel.thumbnail,
                comments=koreanhotel.comments,
                price=koreanhotel.price,
                detail_url=koreanhotel.detail_url,
            )


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
    detail_url = models.CharField(max_length=250, blank=True)




class KoreanHotelDetail(models.Model):
    korean_hotel = models.ForeignKey(KoreanHotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    pictures = models.CharField(max_length=500, blank=True)
    infos = models.CharField(max_length=500, blank=True)
