# coding: UTF-8
from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render

from cms.models import Duelist

def index(request):
    Datetime = {
        'hour': datetime.now().hour,
    }
    return render(request, 'index.html', Datetime)

def tournament_list(request):
    """試合の一覧"""
    return HttpResponse('試合の一覧')

def duelist_list(request):
    """参加者の一覧"""
    duelists = Duelist.objects.all().order_by('id')
    return render(request,
                  'cms/duelist_list.html',
                  {'duelists': duelists})

def duelist_edit(request):
    """参加者の編集"""
    return HttpResponse('参加者の編集')

def duelist_del(request):
    """参加者の削除"""
    return HttpResponse('参加者の削除')


# Create your views here.
