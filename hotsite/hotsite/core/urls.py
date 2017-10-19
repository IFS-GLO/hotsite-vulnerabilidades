from django.conf.urls import url

from hotsite.panel.views import login
from hotsite.posts.views import post, category
from .views import *

urlpatterns = [
    url('^$', index, name='index'),
    url('^login/$', login, name='login'),

    url('^catalog/$', catalog, name='catalog'),

    url('^vulnerability/(?P<pk>\w+)/$', vulnerability, name="vulnerability"),

    url('^providers/$', providers, name="providers"),
    url('^provider/(?P<pk>\w+)/$', provider, name="provider"),

    url('^products/$', products, name="products"),
    url('^product/(?P<pk>\w+)/$', product, name="product"),

    url('^category/(?P<category_slug>[\w-]+)/', category, name="category"),
    url('^article/(?P<category_slug>[\w-]+)/(?P<post_slug>[\w-]+)/', post, name="post"),
]
