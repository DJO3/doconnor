from django.conf.urls import patterns, url
from blog import views, feed



urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^tag/(?P<slug>\S+)$', views.TagIndex.as_view(), name="tag_index"),
    url(r'^feed/$', feed.LatestPosts(), name='feed'),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^about/$', views.about, name='about'),
    url(r'^edu/$', views.edu, name='edu'),

)