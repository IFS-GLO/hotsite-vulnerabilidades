from django.conf.urls import url, include

urlpatterns = [
    url('^', include('hotsite.core.urls', namespace='core')),
]
