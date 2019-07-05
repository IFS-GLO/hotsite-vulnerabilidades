from django.conf.urls import url, include

from .views import *


app_name = 'panel'

urlpatterns = [

    url('^login/$', login, name='login'),
    url('^logout/$', logout, name='logout'),

    url('^catalog/', include('hotsite.catalog.urls', namespace='catalog')),

    url('^posts/', include('hotsite.posts.urls', namespace='posts')),

    url('^$', index, name='index'),
]

