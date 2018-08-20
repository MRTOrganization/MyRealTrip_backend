from django.conf import settings
from django.db import models

from products import crawler
from region.models import Country

__all__ = (
    'PopularCity',
)

class PopularCity(models.Model):
    popular_image = models.ImageField(upload_to='popular-city-image', blank=True)
    popular_city_name = models.CharField(max_length=255)
    # crwaler를 실행하여 popular_city_list를 반환함
    def get_popular_city_crawler(self):
        popular_city_list = crawler.GetPopularCity().get_popular_city_list()
        return popular_city_list

    # 위 함수를 실행시켜 얻은 popular_city_list를 통해 각 유명도시 인스턴스 생성
    def create_popular_city(self):
        city_list = self.get_popular_city_crawler()
        for city in city_list:
            PopularCity.objects.create(
                popular_image=city['popular_image'],
                popular_city_name=city['popular_city_name'],
            )







