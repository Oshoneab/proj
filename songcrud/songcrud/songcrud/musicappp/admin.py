from django.contrib import admin
from . models import *

class ArtisteAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','age','id']
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'artiste_id','date_released','likes','id']
class LyricAdmin(admin.ModelAdmin):
    list_display = ['content','song_id']
# Register your models here.
admin.site.register(Artiste, ArtisteAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Lyric, LyricAdmin)