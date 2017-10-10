# coding: UTF-8
from django.contrib import admin
from cms.models import Duelist, Tournament, DuelistTournament

class DuelistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mailAddress', 'passward',)
    list_display_link = ('id', 'name', 'mailAddress', 'passward',)

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_link = ('id', 'name',)

class DuelistTournamentAdmin(admin.ModelAdmin):
    list_display = ('id','win', 'lose', 'draw',)
    list_display_link = ('id', 'win', 'lose', 'draw',)

# Register your models here.
admin.site.register(Duelist, DuelistAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(DuelistTournament, DuelistTournamentAdmin)
