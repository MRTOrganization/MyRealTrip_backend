from rest_framework import serializers

from hotels.models import KoreanHotelInfo, KoreanHotel, KoreanHotelDetail


class KHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = KoreanHotelInfo
        fields = (
            'pk',
            'city',
            'country',
        )

class KHotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = KoreanHotel
        fields = (
            'pk',
            'name',
            'city',
            'country',
            'thumbnail',
            'comments',
            'price',
        )

class KHotelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KoreanHotelDetail
        fields = (
            'pk',
            'korean_hotel',
            'name',
            'pictures',
            'infos',
        )
