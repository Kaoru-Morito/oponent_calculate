# coding: UTF-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

class Duelist(models.Model):
    """参加者"""
    name = models.CharField('名前', max_length=255)
    mailAddress = models.CharField('メールアドレス', max_length=100, default="", )
    passward = models.CharField('パスワード', max_length=30, default="",)
    def __str__(self):
        return self.name

class Tournament(models.Model):
    """大会"""
    name = models.CharField('大会名', max_length=255)
    date = models.DateTimeField('開催日', default=datetime.now, blank=True)
    duelists = models.ManyToManyField(Duelist, through='Result')
    def __str__(self):
        return self.name

class Result(models.Model):
    """戦績"""
    win = models.IntegerField('勝ち数', default=0)
    lose = models.IntegerField('負け数', default=0)
    draw = models.IntegerField('引き分け数', default=0)
    duelist = models.ForeignKey(Duelist, verbose_name='参加者', related_name='results')
    tournament = models.ForeignKey(Tournament, verbose_name='大会', related_name='results')
    def __str__(self):
        return "参加者"

