from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from shoplistapp.models import ShopList


def index(request):
    shop_list = ShopList(name = "New Shop List")
    shop_list.save()

    return redirect(shoplist, list_id = shop_list.id)


def shoplist(request, list_id):
    shopList = get_object_or_404(ShopList, pk=list_id)
    return render(request, 'shoplistapp/shoplistName.html', {'shopList': shopList})