from django.conf import settings
from django.db import models

from products import crawler

__all__ = (
    'PopularCityList',
)


class PopularCityList(models.Model):
    popular_image = models.ImageField(upload_to='popular-city-image', blank=True)
    popular_city_name = models.CharField(max_length=10)

    def get_popular_city_crawler(self):
        popular_city_list = crawler.GetPopularCityList(
            popular_image=self.popular_image,
            popular_city_name=self.popular_city_name
        )
        popular_city_list.get_popular_city_list()
        result = popular_city_list.city_list
        print('model', result)
        return result


