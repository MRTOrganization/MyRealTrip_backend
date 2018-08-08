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
            self.no,
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


