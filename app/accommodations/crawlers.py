import requests
from bs4 import BeautifulSoup
import re


class PopularHotelList:
    def __init__(self, city, country):
        self.city = city
        self.country = country
        self.popularhotel_list = list()
        self.popularcity_list = list()

    def search_popularhotel(self):
        params = {'city': self.city, 'country': self.country}
        response = requests.get('https://www.myrealtrip.com/hotels?', params)
        soup = BeautifulSoup(response.text, 'lxml')

        item_list = soup.select('li.item')
        for item in item_list:
            thumbnail = re.findall('\((\S*)\)', item.select_one('div.img-container > div.image').get('style'))[0]
            hotel_name = item.select_one('div.name').get_text(strip=True)
            if item.select_one('div.hotel-review-score'):
                grade = item.select_one('div.hotel-review-score').get_text(strip=True)
            else:
                grade = '평가 정보가 없어요'
            if item.select_one('div.hotel-review-count'):
                comments = item.select_one('div.hotel-review-count').get_text(strip=True)
            else:
                comments = '평가 정보가 없어요'
            if item.select_one('div.hotel-price-text'):
                price = item.select_one('div.hotel-price-text').get_text(strip=True)
            else:
                price = '미정'

            new_popularhotel = PopularHotelDetail(
                city=self.city,
                country=self.country,
                thumbnail=thumbnail,
                hotel_name=hotel_name,
                grade=grade,
                comments=comments,
                price=price,
            )
            self.popularhotel_list.append(new_popularhotel)

        city_list = soup.select('a.outlink-button-container')
        for city in city_list:
            city_name = city.select_one('div.text').get_text(strip=True)
            popular_booking = city.get('href')

            new_popularcity = PopularCityDetail(
                city_name=city_name,
                popular_booking=popular_booking
            )
            self.popularcity_list.append(new_popularcity)


class PopularHotelDetail:
    def __init__(self, city, country, thumbnail, hotel_name, grade, comments, price):
        self.city = city
        self.country = country
        self.thumbnail = thumbnail
        self.hotel_name = hotel_name
        self.grade = grade
        self.comments = comments
        self.price = price


class PopularCityDetail:
    def __init__(self, city_name, popular_booking):
        self.city_name = city_name,
        self.popular_booking = popular_booking
