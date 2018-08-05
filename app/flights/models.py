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
        flight_list = crawler.Flight(
            origin_k=self.origin,
            destination_k=self.destination,
            depart_date=self.depart_date,
            return_date=self.return_date
        ).search_flight()
        return flight_list


class FlightInfoDetail(models.Model):
    flight = models.ForeignKey(
        FlightInfo,
        on_delete=models.CASCADE,
        null=True,
    )
    depart_date = FlightInfo.depart_date
    return_date = FlightInfo.return_date

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

    def __str__(self):
        return f'{self.depart_date} ~ {self.return_date} 일의 가격 : {self.price}'
