# coding: UTF-8
from __future__ import unicode_literals

from django.db import models


class Tournament(models.Model):
    """大会"""
    name = models.CharField('大会名', max_length=255)
    def __str__(self):
        return self.name

class Duelist(models.Model):
    """参加者"""
    name = models.CharField('名前', max_length=255)
    mailAddress = models.CharField('メールアドレス', max_length=255)
    def __str__(self):
        return self.name

class DuelistTournament(models.Model):
    """大会参加"""
    win = models.IntegerField('勝ち数', default=0)
    lose = models.IntegerField('負け数', default=0)
    draw = models.IntegerField('引き分け数', default=0)
    duelist=models.ForeignKey(Duelist, verbose_name='参加者', related_name='duelistTournaments')
    tournament=models.ForeignKey(Tournament, verbose_name='大会', related_name='duelistTournaments')
    def __str__(self):
        return "大会参加者" 

