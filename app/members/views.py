from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def member_list(request):
    return HttpResponse('member list page')