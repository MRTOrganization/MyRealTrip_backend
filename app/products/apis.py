from rest_framework.response import Response
from rest_framework.views import APIView

from products.models.productinfo import ProductInfo, Product
from products.serializer import ProductSerializer, ProductDetailSerializer


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