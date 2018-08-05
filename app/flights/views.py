from django.shortcuts import render

from flights.models import FlightInfo, FlightInfoDetail


def flight_list(request):
    flights = FlightInfo.objects.all()
    context = {
        'flights':flights,
    }
    return render(request, 'flights/flight_list.html', context)


def flight_detail(request, pk):
    flight_info = FlightInfo.objects.filter(pk=pk)[0]
    flight_info.get_flight_info()
    flight_details = flight_info.flightinfodetail_set.all()
    context = {
        'flight_info':flight_info,
        'flight_details':flight_details,
    }
    return render(request, 'flights/flight_detail.html', context)
