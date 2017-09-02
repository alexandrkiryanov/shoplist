from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<list_id>[0-9]+)/$', views.shoplist_by_id, name='shoplist_by_id'),
    url(r'^(?P<list_uuid>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/$', views.shoplist_by_uuid, name='shoplist_by_uuid'),
]