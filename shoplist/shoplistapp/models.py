from django.db import models


# Create your models here.
class ShopList(models.Model):
    name = models.CharField(max_length=200)


class ShopListItem(models.Model):
    shopList = models.ForeignKey(ShopList, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=200)
    itemChecked = models.BooleanField()
