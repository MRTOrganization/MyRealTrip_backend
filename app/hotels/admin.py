from django.contrib import admin

from hotels.models import KoreanHotel, KoreanHotelInfo, KoreanHotelDetail

admin.site.register(KoreanHotel)
admin.site.register(KoreanHotelInfo)
admin.site.register(KoreanHotelDetail)
