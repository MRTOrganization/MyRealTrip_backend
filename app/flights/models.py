from urllib import parse

from django.db import models

from flights import crawler


class FlightInfo(models.Model):
    origin = models.CharField(max_length=255, blank=True)
    destination = models.CharField(max_length=255, blank=True)
    depart_date = models.CharField(max_length=255, blank=True)
    return_date = models.CharField(max_length=255, blank=True)

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
            '상해/푸동': 'PVG',
            '청도':'TAO',
            '대련':'DLC',
            '홍콩':'HKG',
            '대만/타오위안':'TPE',
            '다낭':'DAD',
            '방콕':'BKK',
            '비엔티엔':'VTE',
            '싱가포르':'SIN',
            '코타키나발루':'BKI',
            '발리':'DPS',
            '씨엠립':'REP',
            '울란바토르':'ULN',
            '뭄바이':'BOM',
            '델리':'DEL',
            '로스엔젤레스':'LAX',
            '라스베가스':'LAS',
            '뉴욕':'NYC',
            '샌프란시스코':'SFO',
            '하와이/호놀룰루':'HNL',
            '밴쿠버':'YVR',
            '토론토':'YTO',
            '몬트리올':'YMQ',
            '상파울로':'SAO',
            '칸쿤':'CUN',
            '산티아고':'SCL',
            '하바나':'HAV',
            '런던':'LON',
            '파리':'PAR',
            '로마':'ROM',
            '마드리드':'MAD',
            '프랑크푸르트':'FRA',
            '암스테르담':'AMS',
            '이스탄불':'IST',
            '모스크바':'MOW',
            '시드니':'SYD',
            '멜버른':'MEL',
            '괌':'GUM',
            '사이판':'SPN',
            '아부다비':'AUH',
            '두바이':'DXB',
            '나이로비':'NBO',
            '케이프타운':'CPT',
            '카이로':'CAI',
        }
        origin_k = self.origin
        destination_k = self.destination
        origin = city_korean_dict[origin_k]
        destination = city_korean_dict[destination_k]

        depart_date = self.depart_date
        return_date = self.return_date

        origin_k = parse.quote(origin_k)
        destination_k = parse.quote(destination_k)
        url = f'http://flights.myrealtrip.com/air/b2c/AIR/MBL/AIRMBLSCH0100100010.k1?initform=RT&domintgubun=I&depctycd={origin}&depctycd={destination}&depctycd=&depctycd=&depctynm={origin_k}&depctynm={destination_k}&depctynm=&depctynm=&arrctycd={destination}&arrctycd={origin}&arrctycd=&arrctycd=&arrctynm={destination_k}&arrctynm={origin_k}&arrctynm=&arrctynm=&depdt={depart_date}&depdt={return_date}&depdt=&depdt=&opencase=N&opencase=N&opencase=N&openday=&openday=&openday=&depdomintgbn=I&tasktype=B2C&servicecacheyn=Y&adtcount=1&chdcount=0&infcount=0&cabinclass=Y&cabinsepflag=Y&preferaircd=&secrchType=FARE&maxprice=&availcount=250&KSESID=air%3Ab2c%3ASELK138RB%3ASELK138RB%3A%3A00'
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
