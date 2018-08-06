from django.db import models

from flights import crawler


class FlightInfo(models.Model):
    origin = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True)
    depart_date = models.CharField(max_length=100)
    return_date = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.destination}행 {self.depart_date} ~ {self.return_date} 일 티켓'

    def get_flight_list(self):
        # crawler의 Flight 인스턴스 생성하여 search_flight 함수 실행
        flight_list = crawler.Flight(
            origin_k=self.origin,
            destination_k=self.destination,
            depart_date=self.depart_date,
            return_date=self.return_date
        ).search_flight()
        # flight_list를 리턴
        return flight_list

    def get_flight_info(self):
        # get_flight_list의 결과를 를 다시 받아서 상세정보를 얻음
        flight_list = self.get_flight_list()
        for flight in flight_list:
            # FlightInfoDetail 객체 생성
            FlightInfoDetail.objects.create(
                flight=self,
                go_airline=flight['go_airline'],
                go_dep_time=flight['go_dep_time'],
                go_dep_airport=flight['go_dep_airport'],
                go_arr_time=flight['go_arr_time'],
                go_arr_airport=flight['go_arr_airport'],
                go_flytime=flight['go_flytime'],
                return_airline=flight['return_airline'],
                return_dep_time=flight['return_dep_time'],
                return_dep_airport=flight['return_dep_airport'],
                return_arr_time=flight['return_arr_time'],
                return_arr_airport=flight['return_arr_airport'],
                return_flytime=flight['return_flytime'],
                price=flight['price'],
            )


class FlightInfoDetail(models.Model):
    flight = models.ForeignKey(
        FlightInfo,
        on_delete=models.CASCADE,
        null=True,
    )

    # 출발편
    go_airline = models.CharField(max_length=50)
    go_dep_time = models.CharField(max_length=50)
    go_dep_airport = models.CharField(max_length=50)
    go_flytime = models.CharField(max_length=50)
    go_arr_time = models.CharField(max_length=50)
    go_arr_airport = models.CharField(max_length=50)

    # 귀국편
    return_airline = models.CharField(max_length=50)
    return_dep_time = models.CharField(max_length=50)
    return_dep_airport = models.CharField(max_length=50)
    return_flytime = models.CharField(max_length=50)
    return_arr_time = models.CharField(max_length=50)
    return_arr_airport = models.CharField(max_length=50)

    # 가격
    price = models.CharField(max_length=50)

