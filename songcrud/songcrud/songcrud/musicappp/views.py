from ast import Pass
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET", "POST"])
def artist_list(request):
    if request.method == "GET":
        artists = Artiste.objects.all()
        serializer = ArtisteSerializer(artists, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        serializers = ArtisteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def unique_artist(request, pk):
    try:
        artiste = Artiste.objects.get(id=pk)
    except  artiste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        

    if request.method == "GET":
        serializer = ArtisteSerializer(artiste)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArtisteSerializer(artiste, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        artiste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        #for songs
@api_view(["GET", "POST"])
def song_list(request):
    if request.method == "GET":
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        serializer = SongSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def unique_song(request, pk):
    try:
        song = Song.objects.get(id=pk)
    except  Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        

    if request.method == "GET":
        serializer = SongSerializer(song)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializers = SongSerializer(song, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(["GET", "POST"])
def lyric_list(request):
    if request.method == "GET":
        lyric = Lyric.objects.all()
        serializer = LyricSerializer(lyric, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        serializer = LyricSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def unique_lyric(request, pk):
    try:
        lyric = Lyric.objects.get(id=pk)
    except  Lyric.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        

    if request.method == "GET":
        serializer = LyricSerializer(lyric)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializers = LyricSerializer(lyric, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        lyric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

#  artists = Artiste.objects.all()
#         serializer = ArtisteSerializer(artists, many=True)
#         return Response(serializer.data)


    