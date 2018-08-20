from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models.productinfo import ProductInfo
from products.serializer import ProductDetailSerializer


class ProductDetail(APIView):
    def get_obejct(self, pk):
        product_info = ProductInfo.objects.get(pk=pk)
        try:
            return ProductInfo.objects.get(pk=pk)
        except ProductInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        products_detail = self.get_obejct(pk).productinfodetail_set.first()
        serializer = ProductDetailSerializer(products_detail)
        return Response(serializer.data)
