from django.conf.urls import url

from .views import category, social_item

urlpatterns = [
    url(r'^category/(?P<slug>[\w-]+)/$', category, name='category'),
    url(r'^category/(?P<slug>[\w-]+)/(?P<id>\d+)/$', social_item, name='social_item'),
]
