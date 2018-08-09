import requests
from bs4 import BeautifulSoup


class KoreanHotelList:
    def __init__(self, city, country):
        self.city = city
        self.country = country
        self.koreanhotel_list = list()

    def search_koreanhotel(self):
        params = {'city': self.city, 'country': self.country}
        response = requests.get('https://www.myrealtrip.com/accommodations/lodgings?', params)
        soup = BeautifulSoup(response.text, 'lxml')

        item_list = soup.select('li.item')
        for item in item_list:
            thumbnail = item.select_one('div.img-placeholder > img.img').get('data-echo')
            city_name = item.select_one('div.city-name').get_text(strip=True)
            name = item.select_one('div.name').get_text(strip=True)
            comments = item.select_one('div.review > div.text').get_text(strip=True)
            if item.select_one('div.price'):
                price = item.select_one('div.price').get('data-offer-price')
            else:
                price = '미정'

            new_koreanhotel = KoreanHotelDetail(
                city=self.city,
                country=self.country,
                thumbnail=thumbnail,
                name=name,
                city_name=city_name,
                comments=comments,
                price=price,
            )
            self.koreanhotel_list.append(new_koreanhotel)


class KoreanHotelDetail:
    def __init__(self, city, country, thumbnail, name, city_name, comments, price):
        self.city = city
        self.country = country
        self.thumbnail = thumbnail
        self.name = name
        self.city_name = city_name
        self.comments = comments
        self.price = price
