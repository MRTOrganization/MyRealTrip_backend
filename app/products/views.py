from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponseRedirect


from products.models import PopularCity
from products.models.productinfo import Product, ProductInfo, ProductDetail, ProductDetailInfo
from region.models import Country, City
from wishlist.models import WishList


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
    products = Product.objects.filter(country=Country.objects.get(name=country)).filter(
        city=City.objects.get(name=city))
    if len(products) == 0:
        product_info = ProductInfo.objects.create(country=Country.objects.get(name=country), city=City.objects.get(name=city))
        product_info.create_product()

    products = Product.objects.filter(country=Country.objects.get(name=country)).filter(
        city=City.objects.get(name=city))
    # wishlist = WishList.objects.filter(user=request.user).values_list('product', flat=True)
    context = {
        'products':products,
        # 'wishlist':wishlist,
    }
    return render(request, 'products/products_city_content.html', context)


def product_detail(request, country, city, pk):
    product = ProductDetail.objects.filter(country=Country.objects.get(name=country)).filter(city=City.objects.get(name=city)).filter(pk=pk)
    print(product)
    if len(product) == 0:
        product_detail_info = ProductDetailInfo.objects.create(country=Country.objects.get(name=country)).filter(city=City.objects.get(name=city))
        product_detail_info.create_product_detail()

        product = ProductDetail.objects.filter(country=Country.objects.get(name=country)).filter(city=City.objects.get(name=city)).filter(pk=pk)
        # wishlist = WishList.objects.filter(user=request.user).values_list('product', flat=True)
        context = {
            'product': product,
            # 'wishlist': wishlist,
        }
        return render(request, 'products/product_detail.html', context)


def product_wishlist(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        wish_list = WishList.objects.filter(user=request.user, product=product)
        if wish_list:
            wish_list.delete()
        else:
            wish_list = WishList.objects.create(user=request.user)
            wish_list.product.add(product)
        return redirect('index')


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
