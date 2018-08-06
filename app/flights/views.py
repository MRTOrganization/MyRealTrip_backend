from django.shortcuts import render, redirect

from flights.models import FlightInfo


def flight_list(request):
    if request.method == 'POST':
        origin = request.POST['origin']
        destination = request.POST['destination']
        depart_date = request.POST['depart_date']
        return_date = request.POST['return_date']
        flight = FlightInfo.objects.create(
            origin=origin,
            destination=destination,
            depart_date=depart_date,
            return_date=return_date,
        )

        return redirect('flight-list')
    else:
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
