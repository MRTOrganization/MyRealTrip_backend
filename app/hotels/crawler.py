import requests
from bs4 import BeautifulSoup


class KoreanHotelList:
    def __init__(self, city, country):
        self.city = city
        self.country = country
        self.koreanhotel_list = list()

    def search_koreanhotel(self):
        params = {'city': self.city, 'country': self.country}
        response = requests.get('http://www.myrealtrip.com/accommodations/lodgings?', params)
        soup = BeautifulSoup(response.text, 'lxml')

        item_list = soup.select('li.item')
        for item in item_list:
            thumbnail = item.select_one('div.img-placeholder > img.img').get('data-echo')
            city_name = item.select_one('div.city-name').get_text(strip=True)
            name = item.select_one('div.name').get_text(strip=True)
            comments = item.select_one('div.review > div.text').get_text(strip=True)
            get_href = item.select_one('div.card-cover').select_one('a.offer-link').get('href')
            detail_url = f'http://www.myrealtrip.com{get_href}'
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
                detail_url=detail_url,
            )
            self.koreanhotel_list.append(new_koreanhotel)


class KoreanHotelDetail:
    def __init__(self, city, country, thumbnail, name, city_name, comments, price,  detail_url):
        self.city = city
        self.country = country
        self.thumbnail = thumbnail
        self.name = name
        self.city_name = city_name
        self.comments = comments
        self.price = price
        self.detail_url = detail_url

    def search_koreanhotel_detail(self):
        url = self.detail_url
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div_center = soup.select_one('div.content-center-narrow')

        name = div_center.select_one('div.offer-title').get_text(strip=True)
        div_descriptive = div_center.select_one('div.descriptive-image-container')
        pictures_class = div_descriptive.select('picture.descriptive-image')
        picture_list = list()
        for picture in pictures_class:
            picture_list.append(picture.select_one('img.img').get('srcset'))

        div_extra_info = div_center.select_one('div.extra-info-container')
        div_info_box = div_extra_info.select('div.info-box')
        info_dict = dict()
        info_dict['how_to_use_title'] = div_info_box[1].select_one('div.title').get_text(strip=True)
        info_dict['how_to_use_content'] = div_info_box[1].select_one('span').get_text(strip=True)

        info_dict['cancellation_title'] = div_info_box[2].select_one('div.title').get_text(strip=True)
        info_dict['cancellation_content'] = div_info_box[2].select_one('p').get_text(strip=True)
        korean_hotel_detail_info = KoreanHotelDetailInfo(
            name=name,
            picture_list=picture_list,
            info_dict=info_dict,
        )
        return korean_hotel_detail_info

class KoreanHotelDetailInfo:
    def __init__(self, name, picture_list, info_dict):
        self.name = name
        self.picture_list = picture_list
        self.info_dict = info_dict
