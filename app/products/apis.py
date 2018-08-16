from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import PopularCity
from products.models.productinfo import ProductInfo, Product
from products.serializer import ProductSerializer, ProductDetailSerializer, PopularCitySerializer


class PopularCityList(APIView):
    def get(self, request, format=None):
        popular_cities = PopularCity.objects.all()
        serializer = PopularCitySerializer(popular_cities, many=True)
        return Response(serializer.data)

class ProductList(APIView):
    def get(self, request, format=None):
        products = ProductInfo.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get(self, request, country, city, format=None):
        products = Product.objects.filter(country__name__contains=country).filter(city__name__contains=city)
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)


class ProductSearch(generics.ListAPIView):
    def get_queryset(self):
        keyword = self.kwargs['keyword']

        queryset = Product.objects.filter(
            Q(country__name__contains=keyword) |
            Q(city__name__contains=keyword) |
            Q(tour_name__contains=keyword) |
            Q(title__contains=keyword)
        )
        return queryset
    serializer_class = ProductDetailSerializer

