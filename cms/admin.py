from django.contrib import admin
from cms.models import Duelist, Tournament

class DuelistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'win', 'lose', 'draw',)
    list_display_link = ('id', 'name', 'win', 'lose', 'draw',)

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_link = ('id', 'name',)

# Register your models here.
admin.site.register(Duelist, DuelistAdmin)
admin.site.register(Tournament, TournamentAdmin)
