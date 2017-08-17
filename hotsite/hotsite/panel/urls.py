from django.conf.urls import url, include

from .views import *

urlpatterns = [

    url('^login/$', login, name='login'),
    url('^logout/$', logout, name='logout'),

    url('^catalog/', include('hotsite.catalog.urls', namespace='catalog')),

    url('^$', index, name='index'),
]

