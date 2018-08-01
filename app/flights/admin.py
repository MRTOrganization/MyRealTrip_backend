from django.contrib import admin

from flights.models import FlightInfo, FlightPriceInfo

admin.site.register(FlightInfo)
admin.site.register(FlightPriceInfo
                    )