import requests
from bs4 import BeautifulSoup


class ProductList:
    def __init__(self, city, country, thumbnail, tour_name, title, review, price, category, meta_info):
        self.city = city
        self.country = country
        self.thumbnail = thumbnail
        self.tour_name = tour_name
        self.title = title
        self.review = review
        self.price = price
        self.category = category
        self.meta_info = meta_info
        self.ticket_list = list()

    def get_product_list(self):
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

            tour_name = item.select_one('div.profile-name').get_text(strip=True)
            print(tour_name)
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
                tour_name=self.tour_name,
                title=self.title,
                review=self.review,
                price=self.price,
                category=self.category,
                meta_info=self.meta_info
            )

            self.ticket_list.append(new_ticket_list)


class ProductDetail:
    def __init__(self, no, title, region, review, guide_image, guide_name, info_description):
        self.title = title
        self.region = region
        self.review = review
        self.guide_image = guide_image
        self.guide_name = guide_name
        self.info_description = info_description
        self.no = no

    def get_product_detail(self):
        params = {
            'no': self.no,
        }
        response = requests.get('https://www.myrealtrip.com/offers/', params)
        # print(response.text)
        soup = BeautifulSoup(response.text, 'lxml')

        # 상품 제목, 국가정보, 리뷰 수 크롤링
        title_container_list = soup.select('div.common-info-container')

        for container in title_container_list:
            title = container.select_one('div.offer-title').get_text(strip=True)
            print(title)
            region_info = container.select_one('div.inner-container ')
            #     print(region_info)
            review = container.select_one('div.score-container > span.text-gray').get_text(strip=True)
            print(review)

        # 아이콘 크롤
        icon_container = soup.select('.info-icon-container > .icon-item')
        # print(icon_container)
        for icon in icon_container:
            icon_image = icon.select_one('img.icon').get('src')
            print(icon_image)
            icon_small_text = icon.select_one('.text-sm').get_text(strip=True)
            print(icon_small_text)
            icon_bold_text = icon.select_one('.text').get_text(strip=True)
            print(icon_bold_text)

        # 투어 참가 가능 연령 크롤링
        sidebar_notice_title = soup.select_one('.sidebar-inner-box > .notice-title').get_text(strip=True)
        print(sidebar_notice_title)
        sidebar_notice_desc = soup.select_one('.sidebar-inner-box > .notice-desc').get_text(strip=True)
        print(sidebar_notice_desc)

        # 가이드 정보 크롤링
        guide_name_div = soup.select_one('div.guide-name')
        guide_name = guide_name_div.contents[1].get_text(strip=True)
        print(guide_name)

        info_description = soup.select_one('div.guide-description > p').get_text(strip=True)
        print(info_description)

        # iamge_list = soup.select('li.item')

        # 상품 정보 크롤링
        introduce_title = soup.select_one('div.introduce-container > div.title').get_text(strip=True)
        print(introduce_title)
        introduce_more = soup.select_one('div.introduce-container > p').get_text(strip=True)
        print(introduce_more)

        # 코스 소개 크롤
        course = soup.select_one('div.course-container > .offer-inner-container > .content-wrapper')

        course_text = course.select_one('.title').get_text(strip=True)
        print(course_text)

        course_lists = course.select('.course-list > .box > .box-wrapper')
        # print(course_list)

        for course_list in course_lists:
            course_meet_place_time = course_list.get_text(strip=True)
            print(course_meet_place_time)

            course_description = course_list.select_one('.description-container')
            course_description_title = course_description.select_one('.info-title').get_text(strip=True)
            print(course_description_title)
            course_description_p = course_description.select_one('.info-description').get_text(strip=True)
            print(course_description_p)

        # 필수 안내 크롤링
        info_boxes = soup.select('.offer-inner-container > .content-center-narrow > .extra-info-container > .info-box')
        # print(info_boxes)

        for info_box in info_boxes:
            info_title = info_box.select_one('.title').get_text(strip=True)
            print(info_title)
            info_detail = info_box.select_one('p.more').get_text(strip=True)
            print(info_detail)

        # 리뷰 크롤링 (이미지 - 여행자 후기사진 글귀)
        review = soup.select_one('div.review-photo-container')

        review_photo = review.select_one('div.title').get_text(strip=True)
        print(review_photo)

        # 리뷰 크롤링 (여행자 - 후기사진 이미지)
        items = soup.select('.review-photo-container > .item-container > .item')
        for item in items:
            img = item.select_one('img.img')
            if img:
                url = img.get('data-echo')
                print(url)

        # 리뷰 크롤링 (글 - 후기 글귀)
        review_text_i = soup.select('div.review-list')

        for review_t in review_text_i:
            review_text_div = review_t.select_one('div.title')

            # 후기
            review_text = review_text_div.contents[0]
            # 후기 갯수
            review_number = review_text_div.contents[1].get_text(strip=True)
            print(review_text)
            print(review_number)

        # 리뷰 크롤링 (글 - 설명)
        wrapper = soup.select_one('div.review-wrapper')
        stats = soup.select_one('div.stats-title')

        stats_color = stats.contents[0].get_text(strip=True)
        stats_black = stats.contents[1].get_text(strip=True)
        print(stats_color)
        print(stats_black)

        # 리뷰 크롤링 (실제 사용자 리뷰 - 이름, 연령, 내용)
        boxes = wrapper.select('div.review-box')
        for box in boxes:
            rows = box.select('div.review-row')
            row_name_review = rows[0]
            row_age_type_date = rows[1]
            #     print(row_age_type_date)
            row_content = rows[2]

            name = row_name_review.select_one('.name').get_text(strip=True)
            print(name)
            spans = row_age_type_date.select('span')
            spans_age = spans[0].get_text(strip=True)
            print(spans_age)
            spans_desc = spans[2].get_text(strip=True)
            print(spans_desc)

            content = row_content.select_one('p.review-message').get_text(strip=True)
            print(content)


class ProductCategoriesList:
    def __init__(self, city, country, categories,
                 thumbnail, tour_name, title, review, price, category, meta_info):
        self.city = city
        self.country = country
        self.categories = categories
        self.country = country
        self.thumbnail = thumbnail
        self.tour_name = tour_name
        self.title = title
        self.review = review
        self.price = price
        self.category = category
        self.meta_info = meta_info
        self.category_list = list()

    def get_product_categories_list(self):
        params = {
            'city': self.city,
            'country': self.country,
            'group_category': 'experience',
            'categories%5B%5D': self.categories,
            'order': 'popular',
        }

        response = requests.get('https://www.myrealtrip.com/offers?', params)
        soup = BeautifulSoup(response.text, 'lxml')

        lists = soup.select('.list-wrapper > ul.item-container > li.item > .card-cover')

        for category_list in lists:
            thumbnail = category_list.select_one('.img-container > .img-placeholder > img.img').get('data-echo')
            print(thumbnail)
            tour_name = category_list.select_one('.content-box > .guide-container > .profile-name').get_text(strip=True)
            print(tour_name)
            title = category_list.select_one('.content-box > .name').get_text(strip=True)
            print(title)
            review = category_list.select_one('.content-box > .review > .text').get_text(strip=True)
            print(review)
            price = category_list.select_one('.content-box > .price').get_text(strip=True)
            print(price)
            category = category_list.select_one('.content-box > .info-container > .category').get_text(strip=True)
            print(category)
            meta_info = category_list.select_one('.content-box > .info-container > .meta-infos').get_text(strip=True)
            print(meta_info)

            new_category_list = ProductCategoriesList(
                city=self.city,
                country=self.country,
                categories=self.categories,
                thumbnail=self.thumbnail,
                tour_name=self.tour_name,
                title=self.title,
                review=self.review,
                price=self.price,
                category=self.category,
                meta_info=self.meta_info,
            )
            self.category_list.append(new_category_list)
            return category_list
