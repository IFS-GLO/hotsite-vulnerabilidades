from django.conf.urls import url

from .views import *


app_name = 'catalog'

urlpatterns = [

    url('^providers/$', providers, name='providers'),
    url('^provider/$', add_provider, name='add_provider'),
    url('^provider/(?P<pk>\w+)/$', provider, name='provider'),
    url('^provider/(?P<pk>\w+)/del/$', del_provider, name="del_provider"),

    url('^categories/$', categories, name='categories'),
    url('^category/$', add_category, name='add_category'),
    url('^category/(?P<pk>\w+)/$', category, name='category'),
    url('^category/(?P<pk>\w+)/del/$', del_category, name="del_category"),

    url('^softwares/$', softwares, name='softwares'),
    url('^software/$', add_software, name='add_software'),
    url('^software/(?P<pk>\w+)/$', software, name='software'),
    url('^software/(?P<pk>\w+)/del/$', del_software, name="del_software"),

    url('^vulnerabilities/$', vulnerabilities, name='vulnerabilities'),
    url('^vulnerability/$', add_vulnerability, name='add_vulnerability'),
    url('^vulnerability/(?P<pk>\w+)/$', vulnerability, name='vulnerability'),
    url('^vulnerability/(?P<pk>\w+)/del/$', del_vulnerability, name='del_vulnerability'),

    url('^licenses/$', licenses, name='licenses'),
    url('^license/$', add_license, name='add_license'),
    url('^license/(?P<pk>\w+)/$', license, name='license'),
    url('^license/(?P<pk>\w+)/del/$', del_license, name='del_license'),

]
