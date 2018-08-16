from django.contrib.auth import get_user_model
from rest_framework import serializers

from accom_search.models import AccomSearchInfo, AccomSearchInfoDetail

User = get_user_model()

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