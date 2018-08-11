from django.shortcuts import render

from products.models import PopularCity
from products.models.productinfo import ProductList
from region.models import Country


def popular_city_list(request):
    # PopularCity 인스턴스를 생성
    cities = PopularCity.objects.create()
    # create_popular_city 클래스 메소드를 실행
    cities.create_popular_city()
    # PopularCity 객체를 전부 검색
    popular_cities = PopularCity.objects.all()
    context = {
        'popular_cities': popular_cities,
    }
    return render(request, 'products/popular_city_list.html', context)


def product_list(request):
    products = ProductList.objects.create()
    products.create_product_list()

    product_lists = ProductList.objects.all()
    print(product_lists)
    context = {
        'product_lists': product_lists,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    pass
