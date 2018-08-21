from django.db import models


class AccomSearchInfo(models.Model):
    attraction = models.CharField(max_length=255, blank=True)
    checkin = models.CharField(max_length=255, blank=True)
    checkout = models.CharField(max_length=255, blank=True)
    group_adults = models.CharField(max_length=255, blank=True)
    group_children = models.CharField(max_length=255, blank=True)
    no_rooms = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.attraction} 에서 {self.checkin} ~ {self.checkout} 까지'

    def accom_search_url(self):
        city_korean_dict = {
            '오사카': '-240905',
            '후쿠오카': '900047908',
            '라스베가스': '20079110',
            '도쿄': '-246227',
            '로마': '-126693',
            '타이페이': '-2637882',
        }
        attraction_k = self.attraction
        attraction = city_korean_dict[attraction_k]
        checkin = self.checkin
        checkout = self.checkout
        group_adults = self.group_adults
        group_children = self.group_children
        no_rooms = self.no_rooms
        url = f'https://sp.booking.com/searchresults.html?city={attraction}&aid=1138078&label=pcweb-accommodation_hotel_popular_city&checkin={checkin}&checkout={checkout}&group_adults={group_adults}&group_children={group_children}&no_rooms={no_rooms}'
        self.accomsearchinfodetail_set.create(url=url)


class AccomSearchInfoDetail(models.Model):
    accomsearch = models.ForeignKey(
        AccomSearchInfo,
        on_delete=models.CASCADE,
        null=True
    )
    url = models.CharField(max_length=800, blank=True)
