# coding: UTF-8
from django.conf.urls import url
from cms import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^template/$', views.index, name='index'),

    # 大会 
    url(r'^tournament/$', views.tournament_list, name='tournament_list'),
    url(r'^tournament/add$', views.tournament_edit, name='tournament_add'),
    url(r'^tournament/mod(?P<tournament_id>\d+)/$', views.tournament_edit, name='tournament_mod'),
    url(r'^tournament/del(?P<tournament_id>\d+)/$', views.tournament_del, name='tournament_del'),
    url(r'^tournament/duelist(?P<tournament_id>\d+)/$', views.duelists_by_tournament, name='duelists_by_tournament'),

    # 参加者
    url(r'^duelist/$', views.duelist_list, name='duelist_list'),
    url(r'^duelist/add/$', views.duelist_edit, name='duelist_add'),
    url(r'^duelist/mod/(?P<duelist_id>\d+)/$', views.duelist_edit, name='duelist_mod'),
    url(r'^duelist/del/(?P<duelist_id>\d+)/$', views.duelist_del, name='duelist_del'),

]

