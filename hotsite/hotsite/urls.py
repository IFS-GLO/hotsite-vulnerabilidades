from django.conf.urls import url, include

urlpatterns = [
    url('^', include('hotsite.core.urls', namespace='core')),
    url('^panel/', include('hotsite.panel.urls', namespace='panel')),
]
