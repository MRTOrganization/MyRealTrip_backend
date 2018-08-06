import requests
from bs4 import BeautifulSoup


class ProductList:
    def __init__(self, city, country, thumbnail, itype, title, review, price, category, meta_info):
        self.city = city
        self.country = country
        self.ticket_list = list()
        self.thumbnail = thumbnail
        self.itype = itype
        self.title = title
        self.review = review
        self.price = price
        self.category = category
        self.meta_info = meta_info

    def product_list(self):
        params = {
            'city': self.city,
            'country': self.country,
        }

        response = requests.get('https://www.myrealtrip.com/offers?', params)
        # print(response.text)
        soup = BeautifulSoup(response.text, 'lxml')

        item_list = soup.select('li.item')
        for item in item_list:
            pre_thumbnail = item.select_one('div.img-placeholder > img.img')
            #     print(pre_thumbnail)
            thumbnail = pre_thumbnail.get('data-echo')
            print(thumbnail)

            itype = item.select_one('div.profile-name').get_text(strip=True)
            print(itype)
            title = item.select_one('div.name').get_text(strip=True)
            print(title)
            review = item.select_one('div.review > div.text').get_text(strip=True)
            print(review)

            price_type = item.select_one('div.price')
            price = price_type.get_text(strip=True)
            print(price)

            category = item.select_one('div.info-container > div.category').get_text(strip=True)
            print(category)

            meta_info = item.select_one('div.meta-infos').get_text(strip=True)
            print(meta_info)

            new_ticket_list = ProductList(
                city=self.city,
                country=self.country,
                thumbnail=self.thumbnail,
                itype=self.itype,
                title=self.title,
                review=self.review,
                price=self.price,
                category=self.category,
                meta_info=self.meta_info
            )

            self.ticket_list.append(new_ticket_list)


class ProductDetail:
    def __init__(self, title, region, review, guide_image, guide_name, info_description):
        self.title = title
        self.region = region
        self.review = review
        self.guide_image = guide_image
        self.guide_name = guide_name
        self.info_description = info_description

    def product_detail(self):
        response = requests.get('https://www.myrealtrip.com/offers/21886')
        # print(response.text)
        soup = BeautifulSoup(response.text, 'lxml')

        title_container_list = soup.select('div.common-info-container')
        # print(container_list)

        for container in title_container_list:
            title = container.select_one('div.offer-title').get_text(strip=True)
            print(title)
            region_info = container.select_one('div.inner-container ')
            #     print(region_info)
            review = container.select_one('div.score-container > span.text-gray').get_text(strip=True)
            print(review)

        icon_container_list = soup.select('div.info-icon-container')
        # print(icon_container_list)
        # for container2 in icon_container_list:

        #     product_type_img = container2.select_one('div.icon-item > img.icon').get('src')
        #     print(product_type_img)
        #     product_type_text_sm = container2.select_one('div.icon-item > div.text-sm').get_text(strip=True)
        #     print(product_type_text_sm)
        #     product_type_text_bold = container2.select_one('div.icon-item > div.text').get_text(strip=True)
        #     print(product_type_text_bold)

        #     meet_time_img = container2.select_one('div.icon-item > img.icon').get('src')
        #     print(meet_time_img)
        #     meet_time_text_sm = container2.select_one('div.text-sm').get_text(strip=True)
        #     print(meet_time_text_sm)

        guide_name_div = soup.select_one('div.guide-name')
        guide_name = guide_name_div.contents[1].get_text(strip=True)
        print(guide_name)

        info_description = soup.select_one('div.guide-description > p').get_text(strip=True)
        print(info_description)

        # iamge_list = soup.select('li.item')

        introduce_title = soup.select_one('div.introduce-container > div.title').get_text(strip=True)
        print(introduce_title)
        introduce_more = soup.select_one('div.introduce-container > p').get_text(strip=True)
        print(introduce_more)

        review_list = soup.select_one('div.review-container')
        # print(review_list)
        # for review in review_list:
        # #     print(review)
        photo_review = review_list.select_one('div.title').get_text(strip=True)
        print(photo_review)
        # review = soup.select_one('div.content-center-narrow > div.title').get_text(strip=True)
        # print(review)
