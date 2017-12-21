from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from django.conf.urls import patterns, include, url
from music.views import MusicListView, MusicByIdView
from category.views import CategoryByIdView, CategoryListView

# router = routers.DefaultRouter()
# router.register(r'posts', PostViewSet, base_name='post')
# router.register(r'queries', QueryViewSet, base_name='query')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/', include(router.urls))
    url(r'^api/music/list/$', MusicListView.as_view()),
    url(r'^api/music/(?P<pk>[0-9]+)/$', MusicByIdView.as_view()),
    url(r'^api/categories/$', CategoryListView.as_view()),
    url(r'^api/category/(?P<pk>[0-9]+)/$', CategoryByIdView.as_view()),
]
