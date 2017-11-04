# coding: UTF-8
from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from cms.models import Duelist, Tournament, Result
from cms.forms import DuelistForm, TournamentForm

def index(request):
    tournaments = Tournament.objects.all().order_by('id')
    return render(request, 'index.html', Tournaments)

def tournament_list(request):
    """大会の一覧"""
    tournaments = Tournament.objects.all().order_by('id')
    return render(request,
                'cms/tournament_list.html',
                {'tournaments': tournaments})

def tournament_edit(request, tournament_id=None):
    """大会の編集"""
    if tournament_id: # tournament_id が指定されている(修正時)
        tournament = get_object_or_404(Tournament, pk=tournament_id)
    else:          # tournament_id が指定されていない(追加時)
        tournament = Tournament()

    if request.method == 'POST':
        form = TournamentForm(request.POST, instance=tournament) # POST されたrequest データからフォームを作成
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.save()
            return redirect('cms:tournament_list')
    else:    #GETの時
        form = TournamentForm(instance=tournament) 

        return render(request, 'cms/tournament_edit.html', dict(form=form, tournament_id=tournament_id))

def tournament_del(request, tournament_id):
    """大会の削除"""
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    tournament.delete()
    return redirect('cms:tournament_list')

def duelist_list(request):
    """参加者の一覧"""
    duelists = Duelist.objects.all().order_by('id')
    return render(request,
                  'cms/duelist_list.html',
                  {'duelists': duelists})

def duelist_edit(request, duelist_id=None):
    """参加者の編集"""
    if duelist_id: # duelist_id が指定されている(修正時)
        duelist = get_object_or_404(Duelist, pk=duelist_id)
    else:          # duelist_id が指定されていない(追加時)
        duelist = Duelist()

    if request.method == 'POST':
        form = DuelistForm(request.POST, instance=duelist) # POST されたrequest データからフォームを作成
        if form.is_valid():
            duelist = form.save(commit=False)
            duelist.save()
            return redirect('cms:duelist_list')
    else:    #GETの時
        form = DuelistForm(instance=duelist) # duelist インスタンスからフォームを作成

        return render(request, 'cms/duelist_edit.html', dict(form=form, duelist_id=duelist_id))

def duelist_del(request, duelist_id):
    """参加者の削除"""
    duelist = get_object_or_404(Duelist, pk=duelist_id)
    duelist.delete()
    return redirect('cms:duelist_list')

def duelists_by_tournament(request, tournament_id):
    """大会参加者"""
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    duelists = tournament.duelists.all()
    return render(request,
                'cms/duelist_list.html',
                {'duelists' : duelists, 'tournament' : tournament})

