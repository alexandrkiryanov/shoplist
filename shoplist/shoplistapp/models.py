from django.db import models
import uuid


# Create your models here.
class ShopList(models.Model):
    name = models.CharField(max_length=200)
    uuid = models.CharField(max_length=40, default='')

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.uuid = str(uuid.uuid4())

        super(ShopList, self).save(args, kwargs)


class ShopListItem(models.Model):
    shopList = models.ForeignKey(ShopList, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=200)
    itemChecked = models.BooleanField()
