from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'yunsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.post_list, name='post_list'),
]
