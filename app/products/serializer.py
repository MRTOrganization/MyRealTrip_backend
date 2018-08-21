from rest_framework import serializers

from products.models import PopularCity
from products.models.productinfo import ProductInfo, Product, ProductDetailBase, ProductTicketDetail, \
    ProductGuideTourDetail, ProductActivityDetail, ProductDetail
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
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = (
            'pk',
            # 'product',
            'title',
            'review_number',
            'product_type_icon',
            'product_type_text',
            # 'date',
            'photo_review',
            'text_review',
            # 'guide_name',
            # 'guide_description',
            'necessary_guide',
        )


class ProductTicketDetailSerializer(ProductDetailSerializer):
    region = CitySerializer()

    class Meta:
        model = ProductTicketDetail
        fields = (
            'region',
            'select_option',
            'info_photo',
            'information',
        )


class ProductGuideTourDetailSerializer(serializers.ModelSerializer):
    region = CitySerializer()

    class Meta:
        model = ProductGuideTourDetail
        fields = (
            'pk',
            'region',
            'tour_terms',
            'course_image',
            'course_text',
        )


class ProductActivityDetailSerializer(serializers.ModelSerializer):
    # detail = ProductDetailSerializer()
    region = CitySerializer()

    class Meta:
        model = ProductActivityDetail
        fields = (
            'pk',
            'region',
            'course_image',
            'course_text',
        )


class ProductSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (

        )
