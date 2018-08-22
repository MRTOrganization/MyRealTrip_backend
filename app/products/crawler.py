import requests
from bs4 import BeautifulSoup


class GetPopularCity:
    def get_popular_city_list(self):
        response = requests.get('https://www.myrealtrip.com/experiences')
        soup = BeautifulSoup(response.text, 'lxml')
        populars = soup.select(
            '.popular_cities__container > .swiper-container > .swiper-wrapper > .swiper-slide > a.popular_cities__item')

        # 결과를 담을 리스트
        popular_city_list = list()

        for popular in populars:

            popular_image = popular.select_one('.popular_cities__item_top').get('style')[22:-1]
            print(popular_image)
            popular_city_name = popular.select_one(
                '.popular_cities__item_bottom > span.popular_cities__item__name').get_text(strip=True)

            # dict에 해당 결과를 담음
            popular_city_dict = dict()
            popular_city_dict['popular_image'] = popular_image
            popular_city_dict['popular_city_name'] = popular_city_name

            # popular_city_list에 결과 dict를 추가함
            popular_city_list.append(popular_city_dict)
        return popular_city_list


class Product:
    def __init__(self, city, country, thumbnail, tour_name, title, review, price, category, meta_info, no):
        self.city = city
        self.country = country
        self.thumbnail = thumbnail
        self.tour_name = tour_name
        self.title = title
        self.review = review
        self.price = price
        self.category = category
        self.meta_info = meta_info
        self.no = no


class ProductList:
    def __init__(self, city, country):
        self.city = city
        self.country = country
        self.product_list = list()

    def get_product_list(self):
        params = {
            'city': self.city,
            'country': self.country,
        }

        response = requests.get('https://www.myrealtrip.com/offers?', params)
        soup = BeautifulSoup(response.text, 'lxml')

        item_list = soup.select('li.item')
        for item in item_list:
            pre_thumbnail = item.select_one('div.img-placeholder > img.img')
            #     print(pre_thumbnail)
            thumbnail = pre_thumbnail.get('data-echo')

            tour_name = item.select_one('div.profile-name').get_text(strip=True)
            title = item.select_one('div.name').get_text(strip=True)
            review = item.select_one('div.review > div.text').get_text(strip=True)

            price_type = item.select_one('div.price')
            price = price_type.get_text(strip=True)

            category = item.select_one('div.info-container > div.category').get_text(strip=True)

            meta_info = item.select_one('div.meta-infos').get_text(strip=True)
            no = item.get('data-offer-id')
            new_product_list = Product(
                city=self.city,
                country=self.country,
                thumbnail=thumbnail,
                tour_name=tour_name,
                title=title,
                review=review,
                price=price,
                category=category,
                meta_info=meta_info,
                no=no,
            )

            self.product_list.append(new_product_list)

        return self.product_list


class ProductDetail:
    def __init__(self, no, title, region, review, product_type, meet_time, time, language,
                 product_type_a, meet_time_a, time_a, language_a, guide_name, guide_desc, introduce, introduce_desc):
        self.no = no
        self.title = title
        self.region = region
        self.review = review
        self.product_type = product_type
        self.meet_time = meet_time
        self.time = time
        self.language = language
        self.product_type_a = product_type_a
        self.meet_time_a = meet_time_a
        self.time_a = time_a
        self.language_a = language_a
        self.guide_name = guide_name
        self.guide_desc = guide_desc
        self.introduce = introduce
        self.introduce_desc = introduce_desc


class GetProductDetail:
    def __init__(self, no):
        self.no = no
        self.product_detail = list()

    def get_product_detail(self):

        url = f'https://www.myrealtrip.com/offers/{self.no}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        dict_result = dict()

        dict_result['title'] = soup.select('.offer-title')[0].get_text(strip=True)
        dict_result['region'] = soup.select('span.text-gray')[0].get_text(strip=True)
        dict_result['review'] = soup.select('span.text-gray')[1].get_text(strip=True)

        dict_result['product_type'] = soup.select('.info-icon-container > .icon-item > .text-sm')[0].get_text(strip=True)
        dict_result['meet_time'] = soup.select('.info-icon-container > .icon-item > .text-sm')[1].get_text(strip=True)
        dict_result['time'] = soup.select('.info-icon-container > .icon-item > .text-sm')[2].get_text(strip=True)
        dict_result['language'] = soup.select('.info-icon-container > .icon-item > .text-sm')[3].get_text(strip=True)

        dict_result['product_type_a'] = soup.select_one('.info-icon-container > .icon-item > .text').get_text(strip=True)
        dict_result['meet_time_a'] = soup.select('.info-icon-container > .icon-item > .text')[1].get_text(strip=True)
        dict_result['time_a'] = soup.select('.info-icon-container > .icon-item > .text')[2].get_text(strip=True)
        dict_result['language_a'] = soup.select('.info-icon-container > .icon-item > .text')[3].get_text(strip=True)


        dict_result['guide_name'] = soup.select_one(
            '.guide-container > .profile-detail > .guide-name > a.gtm-offer-guide-profile > span').get_text(strip=True)
        dict_result['guide_desc'] = soup.select_one('.guide-container > .guide-description > p.more').get_text(strip=True)

        dict_result['introduce'] = soup.select_one('.introduce-container > .title').get_text(strip=True)
        dict_result['introduce_desc'] = soup.select_one('.introduce-container > p.more').get_text(strip=True)


        return dict_result

        # self.product_detail.append(new_product_detail_list)





# class ProductCategoriesList:
#     def __init__(self, city, country, categories,
#                  thumbnail, tour_name, title, review, price, category, meta_info):
#         self.city = city
#         self.country = country
#         self.categories = categories
#         self.country = country
#         self.thumbnail = thumbnail
#         self.tour_name = tour_name
#         self.title = title
#         self.review = review
#         self.price = price
#         self.category = category
#         self.meta_info = meta_info
#         self.category_list = list()
#
#     def get_product_categories_list(self):
#         params = {
#             'city': self.city,
#             'country': self.country,
#             'group_category': 'experience',
#             'categories%5B%5D': self.categories,
#             'order': 'popular',
#         }
#
#         response = requests.get('https://www.myrealtrip.com/offers?', params)
#         soup = BeautifulSoup(response.text, 'lxml')
#
#         lists = soup.select('.list-wrapper > ul.item-container > li.item > .card-cover')
#
#         for category_list in lists:
#             thumbnail = category_list.select_one('.img-container > .img-placeholder > img.img').get('data-echo')
#             tour_name = category_list.select_one('.content-box > .guide-container > .profile-name').get_text(strip=True)
#             title = category_list.select_one('.content-box > .name').get_text(strip=True)
#             review = category_list.select_one('.content-box > .review > .text').get_text(strip=True)
#             price = category_list.select_one('.content-box > .price').get_text(strip=True)
#             category = category_list.select_one('.content-box > .info-container > .category').get_text(strip=True)
#             meta_info = category_list.select_one('.content-box > .info-container > .meta-infos').get_text(strip=True)
#
#             new_category_list = ProductCategoriesList(
#                 city=self.city,
#                 country=self.country,
#                 categories=self.categories,
#                 thumbnail=self.thumbnail,
#                 tour_name=self.tour_name,
#                 title=self.title,
#                 review=self.review,
#                 price=self.price,
#                 category=self.category,
#                 meta_info=self.meta_info,
#             )
#             self.category_list.append(new_category_list)
#             return category_list