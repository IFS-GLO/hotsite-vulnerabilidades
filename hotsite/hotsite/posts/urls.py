from django.conf.urls import url

from .views import *

urlpatterns = [
    url('^category/add/$', add_category, name='add_category'),
    url('^post/add/$', add_post, name='posts'),
]
