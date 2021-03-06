from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponseRedirect

from products.crawler import GetProductDetail
from products.models import PopularCity
from products.models.productinfo import Product, ProductInfo, ProductDetail
from region.models import Country, City
from wishlist.models import WishList


def popular_city_list(request):

    if len(PopularCity.objects.all()) == 0:
        cities = PopularCity.objects.create()
        cities.create_popular_city()
    popular_cities = PopularCity.objects.all()[1:]
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
    products = Product.objects.filter(country=Country.objects.get(name=country)).filter(
        city=City.objects.get(name=city))
    if len(products) == 0:
        product_info = ProductInfo.objects.create(country=Country.objects.get(name=country), city=City.objects.get(name=city))
        product_info.create_product()

    products = Product.objects.filter(country=Country.objects.get(name=country)).filter(
        city=City.objects.get(name=city))


    context = {
        'products':products,
        # 'wishlist':wishlist,
    }
    return render(request, 'products/products_city_content.html', context)


def product_detail(request, country, city, pk):
    product = ProductDetail.objects.filter(
        product__country__name__contains=country,
        product__city__name__contains=city,
        product=Product.objects.get(pk=pk)
    )

    if len(product) == 0:
        instance = Product.objects.get(pk=pk)
        instance.create_product_detail()

    product = ProductDetail.objects.filter(
        product__country__name__contains=country,
        product__city__name__contains=city,
        product=Product.objects.get(pk=pk)
    )[0]

    context = {
        'product': product,

    }
    return render(request, 'products/product_detail.html', context)


def product_search(request):
    keyword = request.GET['keyword']
    if keyword:
        results = Product.objects.filter(
            Q(country__name__contains=keyword)|
            Q(city__name__contains=keyword)|
            Q(tour_name__contains=keyword)|
            Q(title__contains=keyword)
        )
        if len(results) == 0:
            return render(request, 'products/products_search_not_found.html')
        else:
            context = {
                'results':results,
            }
            return render(request, 'products/products_search_result.html', context)
    else:
        return redirect('popular-city-list')