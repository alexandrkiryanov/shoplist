from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from shoplistapp.models import ShopList


class IndexViewTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/shoplist/1/')

        shop_list = ShopList.objects.get(pk=1)
        self.assertEqual('New Shop List', shop_list.name)

        self.assertEqual(3, shop_list.shoplistitem_set.count())
