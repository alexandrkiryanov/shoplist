from django.forms import forms, ModelForm

from shoplistapp.models import ShopList


class ShopListForm(ModelForm):
    class Meta:
        model = ShopList
        exclude = ('uuid',)

