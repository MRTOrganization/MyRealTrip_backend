from django.shortcuts import render

from products.models.product_city_list import PopularCityList
from region.models import Country


def popular_city_list(request):
    popular_cities = PopularCityList.objects.all()
    print(popular_cities)
    context = {
        'popular_cities': popular_cities,
    }
    return render(request, 'products/popular_city_list.html', context)


def product_list(request):
    product_lists = Country.objects.all()
    context = {
        'product_lists': product_lists,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    pass
