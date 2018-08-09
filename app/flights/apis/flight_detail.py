from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from flights.models import FlightInfo
from flights.serializer import FlightDetailSerializer


class FlightDetail(APIView):
    def get_obejct(self, pk):
        flight_info = FlightInfo.objects.get(pk=pk)
        flight_info.get_flight_url()
        try:
            return FlightInfo.objects.get(pk=pk)
        except FlightInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        flight_detail = self.get_obejct(pk).flightinfodetail_set.first()
        serializer = FlightDetailSerializer(flight_detail)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        flight_detail = self.get_obejct(pk).flightinfodetail_set.first()
        flight_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
