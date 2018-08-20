from rest_framework.response import Response
from rest_framework.views import APIView

from accommodations.models import PopularHotelInfo, PopularHotel
from accommodations.serializer import PHotelSerializer, PHotelDetailSerializer


class AccommodationsList(APIView):
    def get(self, request, format=None):
        accommodations = PopularHotelInfo.objects.all()
        serializer = PHotelSerializer(accommodations, many=True)
        return Response(serializer.data)


class AccommodationsDetail(APIView):
    def get(self, request, country, city, format=None):
        accommodations = PopularHotel.objects.filter(country__name__contains=country).filter(city__name__contains=city)
        serializer = PHotelDetailSerializer(accommodations, many=True)
        return Response(serializer.data)
