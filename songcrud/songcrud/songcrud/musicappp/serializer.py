from rest_framework import serializers 
# from musicapp.models import Artiste, Song, Lyrics
from .models import *

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['id', 'first_name', 'last_name', 'age']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artiste_id', 'date_released', 'likes']

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['id', 'song_id', 'content']

