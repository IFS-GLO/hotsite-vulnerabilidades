from django.conf.urls import url

from .views import *

urlpatterns = [

    url('^providers/$', providers, name='providers'),
    url('^provider/$', add_provider, name='add_provider'),
    url('^provider/(?P<pk>\w+)$', provider, name='provider'),

]
