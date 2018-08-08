from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from flights.models import FlightInfo
from flights.serializer import FlightSerializer, FlightDetailSerializer


class FlightList(APIView):
    def get(self, request, format=None):
        flights = FlightInfo.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_flight = FlightInfo.objects.latest('pk')
            new_flight.get_flight_url()
            detail_serializer = FlightDetailSerializer(new_flight.flightinfodetail_set.first())
            return Response(detail_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
