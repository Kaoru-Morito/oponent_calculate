# coding: UTF-8
from django.forms import ModelForm
from cms.models import Duelist
from cms.models import Tournament


class DuelistForm(ModelForm):
    """参加者のフォーム"""
    class Meta:
        model = Duelist
        fields = ('name', )

class TournamentForm(ModelForm):
    """大会のフォーム"""
    class Meta:
        model = Tournament 
        fields = ('name', )
