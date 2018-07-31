from django.db import models
from products.models import TicketInfo, GuideTourInfo, ActivityInfo
from hotels.models import KoreanHotel


class ReservationBase(models.Model):
    phone_number = models.CharField(max_length=10)
    travel_concept = models.CharField(max_length=30)
    requirement = models.TextField()

    class Meta:
        abstract = True


class TicketReservation(ReservationBase):
    ticket = models.ManyToManyField(
        TicketInfo,
        related_name=''
    )
    email = models.EmailField()
    email2 = models.EmailField()


class GuideTourReservation(ReservationBase):
    guide = models.ManyToManyField(
        GuideTourInfo,
        related_name=''
    )


class KoreanHotelReservation(ReservationBase):
    GENDER_CHOICE = (
        ('m', '남성'),
        ('f', '여성'),
        ('x', '선택안함'),
    )
    korean_hotel = models.ManyToManyField(
        KoreanHotel,
        related_name=''
    )
    english_first_name = models.CharField(max_length=10)
    english_last_name = models.CharField(max_length=10)
    korean_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICE)
    birth = models.CharField(max_length=10)
    arrived_time = models.CharField(max_length=10)


class ActivityReservation(ReservationBase):
    activity = models.ManyToManyField(
        ActivityInfo,
        related_name=''
    )
