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
    name = models.CharField(max_length=255, blank=True)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )
    thumbnail = models.CharField(max_length=255, blank=True)
    comments = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=True)
    detail_url = models.CharField(max_length=255, blank=True)

    def create_koreanhotel_detail(self):
        koreanhotel = crawler.KoreanHotelDetailCrwaling(
            city=self.city,
            country=self.country,
            thumbnail=self.thumbnail,
            name=self.name,
            city_name=self.city_name,
            comments=self.comments,
            price=self.price,
            detail_url=self.detail_url
        )
        koreanhotel_detail_info = koreanhotel.search_koreanhotel_detail()
        new_koreanhotel_detail = KoreanHotelDetail.objects.create(
            korean_hotel=self,
            name=koreanhotel_detail_info.name,
            pictures=koreanhotel_detail_info.picture_list,
            infos=koreanhotel_detail_info.info_dict,
        )
        return new_koreanhotel_detail



class KoreanHotelDetail(models.Model):
    korean_hotel = models.ForeignKey(KoreanHotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    pictures = models.CharField(max_length=500, blank=True)
    infos = models.CharField(max_length=500, blank=True)
