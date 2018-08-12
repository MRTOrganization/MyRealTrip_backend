from rest_framework import serializers

from products.models import PopularCity
from products.models.productinfo import ProductInfo, Product


class PopularCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularCity
        fields = (
            'pk',
            'popular_image',
            'popular_city_name',
        )

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
