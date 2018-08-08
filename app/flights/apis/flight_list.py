from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from flights.models import FlightInfo
from flights.serializer import FlightSerializer


class FlightList(APIView):
    def get(self, request, format=None):
        flights = FlightInfo.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
