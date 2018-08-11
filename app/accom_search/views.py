from django.shortcuts import render


def search_list(request):
    return render(request, 'accom_search/search_list.html')
