from django.conf.urls import url

from .views import *


app_name = 'posts'

urlpatterns = [
    url('^categories/$', categories, name='categories'),
    url('^category/add/$', add_category, name='add_category'),
    url('^category/(?P<category_slug>[\w-]+)/$', category, name='category'),

    url('^posts/$', posts, name='posts'),
    url('^post/add/$', add_post, name='add_post'),
    url('^post/(?P<post_slug>[\w-]+)/$', post, name='post'),
]
