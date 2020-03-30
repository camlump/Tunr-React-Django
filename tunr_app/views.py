from django.shortcuts import render
from rest_framework import viewsets
from .models import Artist, Song
from .serializers import ArtistSerializer, SongSerializer


class ArtistView(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
