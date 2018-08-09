from django.contrib.auth import get_user_model
from rest_framework import serializers

from flights.models import FlightInfo, FlightInfoDetail

User = get_user_model()


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightInfo
        fields = (
            'pk',
            'origin',
            'destination',
            'depart_date',
            'return_date',
        )

class FlightDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightInfoDetail
        fields = (
            'pk',
            'url',
        )

