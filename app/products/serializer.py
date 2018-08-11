from rest_framework import serializers
from products.models.productinfo import ProductInfo, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = (
            'pk',
            'city',
            'country',
        )

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'pk',
            'city',
            'country',
            'tour_name',
            'thumbnail',
            'title',
            'review',
            'price',
            'category',
            'meta_info',
        )
