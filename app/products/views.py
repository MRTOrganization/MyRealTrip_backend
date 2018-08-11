from django.shortcuts import render

from products.models import PopularCity
from region.models import Country


def popular_city_list(request):

    if len(PopularCity.objects.all()) == 0:
        cities = PopularCity.objects.create()
        cities.create_popular_city()
        popular_cities = PopularCity.objects.all()

    else:
        popular_cities = PopularCity.objects.all()

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
