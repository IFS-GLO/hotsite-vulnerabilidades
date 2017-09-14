from django.conf.urls import url

from .views import *

urlpatterns = [
    url('^$', index, name='index'),
    url('^catalog/$', catalog, name='catalog'),

    url('^vulnerability/(?P<pk>\w+)/$', vulnerability, name="vulnerability"),

    url('^providers/$', providers, name="providers"),
    url('^provider/(?P<pk>\w+)/$', provider, name="provider"),

    url('^products/$', products, name="products"),
    url('^product/(?P<pk>\w+)/$', product, name="product"),
]
