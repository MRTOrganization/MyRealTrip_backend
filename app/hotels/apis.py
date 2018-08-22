from rest_framework.response import Response
from rest_framework.views import APIView

from hotels.models import KoreanHotelInfo, KoreanHotel, KoreanHotelDetail
from hotels.serializer import KHotelSerializer, KHotelDetailSerializer, KHotelInfoSerializer


class HotelList(APIView):
    def get(self, request, format=None):
        hotels = KoreanHotelInfo.objects.all()
        serializer = KHotelSerializer(hotels, many=True)
        return Response(serializer.data)

class HotelDetail(APIView):
    def get(self, request, country, city, format=None):
        hotels = KoreanHotel.objects.filter(country__name__contains=country).filter(city__name__contains=city)
        serializer = KHotelDetailSerializer(hotels, many=True)
        return Response(serializer.data)

class HotelInfo(APIView):
    def get(self, request, country, city, pk, format=None):
        hotels = KoreanHotelDetail.objects.get(korean_hotel_id=pk)
        serializer = KHotelInfoSerializer(hotels, many=True)
        return Response(serializer.data)