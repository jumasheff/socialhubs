from django.conf.urls import url

from .views import category


urlpatterns = [
	url(r'^category/(?P<slug>[\w-]+)/$', category, name='category')
]
