import requests
from bs4 import BeautifulSoup


class TicketList:
    def __init__(self, city, country):
        self.city = city
        self.country = country
        self.ticket_list = list()

    def search_ticket(self):
        params = {
            'city': self.city,
            'country': self.country,
        }
        response = requests.get('https://www.myrealtrip.com/offers?city=Osaka&country=Japan', params)
        soup = BeautifulSoup(response.text, 'lxml')

        item_list = soup.select('li.item')
        for item in item_list:
            thumbnail = item.select_one('div.img-placeholder > img-small loaded').get('src')
            type = item.select_one('div.profile-name').get_text(strip=True)
            title = item.select_one('div.name').get_text(strip=True)
            review = item.select_one('div.review > div.text').get_text(strip=True)
            unit_price = item.select_one('div.price > span.unit').get_text(strip=True)
            price = item.select_one('div.price > span').get_text(strip=True)
            category = item.select_one('div.info-container > div.category').get_text(strip=True)
            meta_info = item.select_one('div.meta-info').get_text(strip=True)

            new_ticket = TicketDetail(
                city=self.city,
                county=self.country,
                thumbnail=thumbnail,
                type=type,
                title=title,
                review=review,
                unit_price=unit_price,
                price=price,
                category=category,
                meta_info=meta_info,
            )

            self.ticket_list.append(new_ticket)


class TicketDetail:
    def __init__(self, city, county, thumbnail, type, title, review, unit_price, price, category, meta_info):
        self.city = city
        self.country = county
        self.thumbnail = thumbnail
        self.type = type
        self.title = title
        self.review = review
        self.unit_price = unit_price
        self.price = price
        self.category = category
        self.meta_info = meta_info




