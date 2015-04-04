from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown', include('django_markdown.urls')),
    url(r'^', include('blog.urls')),
)
