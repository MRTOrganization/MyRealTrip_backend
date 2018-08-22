from rest_framework import serializers

from products.models import PopularCity
from products.models.productinfo import ProductInfo, Product, ProductDetail
from region.models import City, Country


class PopularCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularCity
        fields = (
            'pk',
            'popular_image',
            'popular_city_name',
        )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'pk',
            'name',
        )


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'pk',
            'name',
        )


class ProductSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    country = CountrySerializer()

    class Meta:
        model = ProductInfo
        fields = (
            'pk',
            'city',
            'country',
        )


class ProductListSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    country = CountrySerializer()

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
            'no',
        )


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetail
        fields = (
            'pk',
            'region',
            'title',
            'review',
            'price',
            'product_type',
            'meet_time',
            'time',
            'language',
            'product_type_a',
            'meet_time_a',
            'time_a',
            'language_a',
            'guide_name',
            'guide_desc',
            'introduce',
            'introduce_desc',
        )


class ProductSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (

        )
