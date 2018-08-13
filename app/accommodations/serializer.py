from rest_framework import serializers

from accommodations.models import PopularHotelInfo, PopularHotel


class PHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularHotelInfo
        fields = (
            'pk',
            'city',
            'country',
        )


class PHotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularHotel
        fields = (
            'pk',
            'name',
            'city',
            'country',
            'thumbnail',
            'comments',
            'price',
        )
