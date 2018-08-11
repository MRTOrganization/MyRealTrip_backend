from django.shortcuts import render

from products.models import PopularCity
from products.models.productinfo import Product, ProductInfo
from region.models import Country, City


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

    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'products/product_list.html', context)


def product_city_content(request, country, city):
    product = ProductInfo.objects.create(country=Country.objects.get(name=country), city=City.objects.get(name=city))
    product.create_product()
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'products/products_city_content.html', context)

def product_detail(request, pk):
    pass
