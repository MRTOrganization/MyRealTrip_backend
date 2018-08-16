from django.contrib import admin

from accommodations.models import PopularHotelInfo, PopularHotel, PopularHotelPriceInfo

admin.site.register(PopularHotel)
admin.site.register(PopularHotelInfo)
admin.site.register(PopularHotelPriceInfo)
