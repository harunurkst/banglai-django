from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^post-list/', views.post_list, name='post-list'),
    url(r'^single-post/(?P<post_id>[0-9]+)/', views.single_post, name='single-post')
]
