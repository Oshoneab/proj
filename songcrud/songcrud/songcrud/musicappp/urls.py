from django.urls import path 
from musicappp import views

urlpatterns = [
    path('artiste', views.artist_list),
    path('artiste/<str:pk>', views.unique_artist),
    path('song', views.song_list),
    path('song/<str:pk>', views.unique_song),
    path('lyric', views.lyric_list),
    path('lyric/<str:pk>', views.unique_lyric),

]