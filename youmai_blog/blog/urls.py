from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'blog.views.archive'),
]