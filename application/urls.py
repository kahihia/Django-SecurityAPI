from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

# Examples:
# url(r'^$', 'settings.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'', include('landing_page.urls')),
	url(r'^admin/', include(admin.site.urls)),
]
