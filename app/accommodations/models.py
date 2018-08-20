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

    def create_popularhotel(self):
        popularhotel_list = self.get_popularhotel_list()
        for popularhotel in popularhotel_list:
            PopularHotel.objects.create(
                city=popularhotel.city,
                country=popularhotel.country,
                thumbnail=popularhotel.thumbnail,
                hotel_name=popularhotel.hotel_name,
                grade=popularhotel.grade,
                comments=popularhotel.comments,
                price=popularhotel.price,
            )

    def get_popularcity_list(self):
        popularcity_list = crawlers.PopularHotelList(
            city=self.city,
            country=self.country,
        )
        popularcity_list.search_popularhotel()
        result1 = popularcity_list.popularcity_list
        return result1


class PopularHotel(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )
    thumbnail = models.CharField(max_length=500, blank=True)
    hotel_name = models.CharField(max_length=255, blank=True)
    grade = models.TextField()
    comments = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=True)


