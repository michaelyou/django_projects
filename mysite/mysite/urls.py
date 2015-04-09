from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mysite.views.first_page'),
    url(r'^west/', include('west.urls')),  
    url(r'^login/', 'west.views.user_login'),
]
