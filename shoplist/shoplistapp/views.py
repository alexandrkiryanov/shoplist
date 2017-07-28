from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from shoplistapp.models import ShopList


def index(request):
    return HttpResponse("Shop List")


def shoplist(request, list_id):
    return HttpResponse(ShopList.objects.get(pk=list_id).name)