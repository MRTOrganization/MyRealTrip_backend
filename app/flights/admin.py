from django.contrib import admin

from flights.models import FlightInfo, FlightInfoDetail

admin.site.register(FlightInfo)
admin.site.register(FlightInfoDetail)