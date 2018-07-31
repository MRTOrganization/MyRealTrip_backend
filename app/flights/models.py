from django.db import models


class FlightInfo(models.Model):
    origin = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True)
    date = models.IntegerField()

    def __str__(self):
        return f'{self.destination}행 {self.date}일 티켓'


class FlightPriceInfo(models.Model):
    flight = models.ForeignKey(
        FlightInfo,
        on_delete=models.CASCADE,
        null=True,
    )
    date = models.IntegerField()
    price = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.date}일의 가격 : {self.price}'
