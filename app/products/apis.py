from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import PopularCity
from products.models.productinfo import ProductInfo, Product
from products.serializer import ProductSerializer, PopularCitySerializer, \
    ProductListSerializer, ProductTicketDetailSerializer, ProductDetailSerializer


class PopularCityList(APIView):
    def get(self, request, format=None):
        popular_cities = PopularCity.objects.all()
        serializer = PopularCitySerializer(popular_cities, many=True)
        return Response(serializer.data)


class ProductCityList(APIView):
    def get(self, request, format=None):
        product_city = ProductInfo.objects.all()
        serializer = ProductSerializer(product_city, many=True)
        return Response(serializer.data)


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)

class ProductListGuide(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(category__contains='가이드 투어')[:6]
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)

class ProductListTicket(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(category__contains='티켓/교통패스')[:6]
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)

class ProductListActivity(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(category__contains='액티비티')[:6]
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)

class ProductListSnapShot(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(category__contains='스냅촬영')[:6]
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)

class ProductListRestaunrant(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(category__contains='레스토랑')[:6]
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)

class ProductListFun(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(category__contains='즐길거리')[:6]
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)

class ProductListConvenience(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(category__contains='여행편의')[:6]
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get(self, request, country, city, format=None):
        print(country)
        print(city)
        products = Product.objects.filter(country__name__contains=country).filter(city__name__contains=city)
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)


# class ProductTicket(APIView):
#     def get(self, request, country, city, format=None):
#         products = Product.objects.filter(country__name__contains=country).filter(city__name__contains=city)
#         serializer = ProductTicketDetailSerializer(products, many=True)
#         return Response(serializer.data)


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

