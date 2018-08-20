from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import PopularCity
from products.serializer import PopularCitySerializer


class PopularCityList(APIView):
    def get(self, request, format=None):
        populars = PopularCity.objects.all()
        serializer = PopularCitySerializer(populars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PopularCitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
