from django.contrib import messages
from django.forms import inlineformset_factory

from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

# Create your views here.
from shoplistapp.form import ShopListForm
from shoplistapp.models import ShopList, ShopListItem

ShopListItemFormSet = inlineformset_factory(ShopList, ShopListItem, fields='__all__', extra=0)


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
    shop_list = get_object_or_404(ShopList, pk=list_id)

    if request.method == 'POST':
        shoplist_form = ShopListForm(request.POST, instance=shop_list)

        if shoplist_form.is_valid():
            shop_list = shoplist_form.save(commit=False)
            formset = ShopListItemFormSet(request.POST, instance=shop_list)
            if formset.is_valid():
                shop_list.save()
                formset.save()
                messages.add_message(request, messages.INFO, _('Shop List saved.'))
        else:
            formset = ShopListItemFormSet(request.POST, instance=shop_list)

    else:
        shoplist_form = ShopListForm(instance=shop_list)
        formset = ShopListItemFormSet(instance=shop_list)

    return render(request, 'shoplistapp/shoplistName.html', {'formset': formset, 'shoplist_form': shoplist_form})