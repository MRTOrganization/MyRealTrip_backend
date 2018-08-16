from django.contrib import admin

from accommodations.models import PopularHotelInfo, PopularHotel

admin.site.register(PopularHotel)
admin.site.register(PopularHotelInfo)
