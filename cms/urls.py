# coding: UTF-8
from django.conf.urls import url
from cms import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^template/$', views.index, name='index'),

    # 参加者
    url(r'^duelist/$', views.duelist_list, name='duelist_add'),
    url(r'^duelist/add/$', views.duelist_edit, name='duelist_add'),
    url(r'^duelist/mod/(?P<duelist_id>\d+)/$', views.duelist_edit, name='duelist_mod'),
    url(r'^duelist/del/(?P<duelist_id>\d+)/$', views.duelist_del, name='duelist_del'),

]

