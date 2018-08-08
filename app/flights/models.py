from urllib import parse

from django.db import models

from flights import crawler


class FlightInfo(models.Model):
    origin = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True)
    depart_date = models.CharField(max_length=100, blank=True)
    return_date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.destination}행 {self.depart_date} ~ {self.return_date} 일 티켓'

    def get_flight_url(self):
        city_korean_dict = {
            '인천': 'ICN',
            '김포': 'GMP',
            '제주': 'CJU',
            '부산': 'PUS',
            '오사카': 'OSA',
            '도쿄': 'TYO',
            '후쿠오카': 'FUK',
            '삿포로': 'SPK',
            '북경': 'BJS',
            '상해/푸동': 'PVG'
        }
        origin_k = self.origin
        destination_k = self.destination
        origin = city_korean_dict[origin_k]
        destination = city_korean_dict[destination_k]

        depart_date = self.depart_date
        return_date = self.return_date

        origin_k = parse.quote(origin_k)
        destination_k = parse.quote(destination_k)
        url = f'http://flights.myrealtrip.com/air/b2c/AIR/INT/AIRINTSCH0100100010.k1?initform=RT&domintgubun=I&depctycd={origin}&depctycd={destination}&depctycd=&depctycd=&depctynm={origin_k}&depctynm={destination_k}&depctynm=&depctynm=&arrctycd={destination}&arrctycd={origin}&arrctycd=&arrctycd=&arrctynm={destination_k}&arrctynm={origin_k}&arrctynm=&arrctynm=&depdt={depart_date}&depdt={return_date}&depdt=&depdt=&opencase=N&opencase=N&opencase=N&openday=&openday=&openday=&depdomintgbn=I&tasktype=B2C&servicecacheyn=Y&adtcount=1&chdcount=0&infcount=0&cabinclass=Y&cabinsepflag=Y&preferaircd=&secrchType=FARE&maxprice=&availcount=250&KSESID=air%3Ab2c%3ASELK138RB%3ASELK138RB%3A%3A00'
        self.flightinfodetail_set.create(url=url)

#     def get_flight_list(self):
#         # crawler의 Flight 인스턴스 생성하여 search_flight 함수 실행
#         flight_list = crawler.Flight(
#             origin_k=self.origin,
#             destination_k=self.destination,
#             depart_date=self.depart_date,
#             return_date=self.return_date
#         ).search_flight()
#         # flight_list를 리턴
#         return flight_list
#
#     def get_flight_info(self):
#         # get_flight_list의 결과를 를 다시 받아서 상세정보를 얻음
#         flight_list = self.get_flight_list()
#
#         for flight in flight_list:
#
#             # FlightInfoDetail 객체 생성
#             FlightInfoDetail.objects.create(
#                 flight=self,
#                 go_airline=flight['go_airline'],
#                 go_dep_time=flight['go_dep_time'],
#                 go_dep_airport=flight['go_dep_airport'],
#                 go_arr_time=flight['go_arr_time'],
#                 go_arr_airport=flight['go_arr_airport'],
#                 go_flytime=flight['go_flytime'],
#                 return_airline=flight['return_airline'],
#                 return_dep_time=flight['return_dep_time'],
#                 return_dep_airport=flight['return_dep_airport'],
#                 return_arr_time=flight['return_arr_time'],
#                 return_arr_airport=flight['return_arr_airport'],
#                 return_flytime=flight['return_flytime'],
#                 price=flight['price'],
#             )
#

class FlightInfoDetail(models.Model):
    flight = models.ForeignKey(
        FlightInfo,
        on_delete=models.CASCADE,
        null=True,
    )
    url = models.CharField(max_length=800, blank=True)

#     # 출발편
#     go_airline = models.CharField(max_length=50)
#     go_dep_time = models.CharField(max_length=50)
#     go_dep_airport = models.CharField(max_length=50)
#     go_flytime = models.CharField(max_length=50)
#     go_arr_time = models.CharField(max_length=50)
#     go_arr_airport = models.CharField(max_length=50)
#
#     # 귀국편
#     return_airline = models.CharField(max_length=50)
#     return_dep_time = models.CharField(max_length=50)
#     return_dep_airport = models.CharField(max_length=50)
#     return_flytime = models.CharField(max_length=50)
#     return_arr_time = models.CharField(max_length=50)
#     return_arr_airport = models.CharField(max_length=50)
#
#     # 가격
#     price = models.CharField(max_length=50)
#
#     class Meta:
#         ordering = ['price']
