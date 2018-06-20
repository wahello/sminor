from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.greinar_list, name='greinar-list'),
    url(r'^add/$', views.greinar_add, name='greinar-add'),
    url(r'^(?P<pk>[0-9]+)/$', views.greinar_details, name='greinar-details'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.greinar_update, name='greinar-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.greinar_delete, name='greinar-delete')]
