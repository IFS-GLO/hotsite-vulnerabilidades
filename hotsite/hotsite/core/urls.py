from django.conf.urls import url

from hotsite.panel.views import login
from hotsite.posts.views import view_post, view_category
from .views import *


app_name = 'core'

urlpatterns = [
    url('^$', catalog, name='index'),
    url('^login/$', login, name='login'),

    url('^catalog/$', catalog, name='catalog'),

    url('^vulnerability/$', index, name='vulnerabilities'),
    url('^vulnerability/(?P<pk>\w+)/$', vulnerability, name="vulnerability"),

    url('^providers/$', providers, name="providers"),
    url('^provider/(?P<pk>\w+)/$', provider, name="provider"),

    url('^products/$', products, name="products"),
    url('^product/(?P<pk>\w+)/$', product, name="product"),

    url('^category/(?P<category_slug>[\w-]+)/', view_category, name="view_category"),
    url('^article/(?P<category_slug>[\w-]+)/(?P<post_slug>[\w-]+)/', view_post, name="view_post"),

    url('^mail/preview/', mail_preview, name='mail_preview'),
]
