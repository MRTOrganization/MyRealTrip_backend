from rest_framework import serializers

from accom_search.models import AccomSearchInfo, AccomSearchInfoDetail


class AccomSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccomSearchInfo
        fields = (
            'pk',
            'attraction',
            'checkin',
            'checkout',
            'group_adults',
            'group_children',
            'no_rooms',
        )


class AccomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccomSearchInfoDetail
        fields = (
            'pk',
            'url',
        )