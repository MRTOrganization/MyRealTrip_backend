from django.contrib import admin

from hotels.models import Hotel, KoreanHotel, KoreanHotelPriceInfo

admin.site.register(Hotel)
admin.site.register(KoreanHotel)
admin.site.register(KoreanHotelPriceInfo)
