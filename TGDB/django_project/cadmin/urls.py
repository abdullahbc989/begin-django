from django.conf.urls import url, include
from cadmin import views

urlpatterns = [
    url(r'/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^post/add/$', views.post_add, name='post_add'),
    url(r'^post/update/(?P<pk>[\d]+)/$', views.post_update, name='post_update'),
]
