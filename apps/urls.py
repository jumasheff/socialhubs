from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	# Home
	url(r'^$', views.home, name='home'),

	# Admin
	url(r'^admin/', include(admin.site.urls)),

	url(r'^', include('apps.social_objects.urls')),

	url(r'^search/$', 'apps.views.search_road_map', name='search_road_map'),

]



from django.conf import settings
from django.conf.urls.static import static
# For serve static, media, templates in develop mode
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static('/templates/', document_root=settings.BASE_DIR + '/templates/')
