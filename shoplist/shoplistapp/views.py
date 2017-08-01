from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from shoplistapp.models import ShopList, ShopListItem


def index(request):
    shop_list = ShopList(name = "New Shop List")
    shop_list.save()

    item1 = ShopListItem(itemName='item1', itemChecked=False)
    item2 = ShopListItem(itemName='item2', itemChecked=False)
    item3 = ShopListItem(itemName='item3', itemChecked=False)

    shop_list.shoplistitem_set.add(item1, bulk=False)
    shop_list.shoplistitem_set.add(item2, bulk=False)
    shop_list.shoplistitem_set.add(item3, bulk=False)

    return redirect(shoplist, list_id=shop_list.id)


def shoplist(request, list_id):
    shopList = get_object_or_404(ShopList, pk=list_id)
    return render(request, 'shoplistapp/shoplistName.html', {'shopList': shopList})