from rest_framework.response import Response
from rest_framework.views import APIView

from hotels.models import KoreanHotelInfo, KoreanHotel
from hotels.serializer import KHotelSerializer, KHotelDetailSerializer


class HotelList(APIView):
    def get(self, request, format=None):
        hotels = KoreanHotelInfo.objects.all()
        serializer = KHotelSerializer(hotels, many=True)
        return Response(serializer.data)

class HotelDetail(APIView):
    def get(self, request, format=None):
        hotels = KoreanHotel.objects.all()
        serializer = KHotelDetailSerializer(hotels, many=True)
        return Response(serializer.data)