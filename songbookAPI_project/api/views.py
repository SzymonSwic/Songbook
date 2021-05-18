from django import forms
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from rest_framework import viewsets

from .serializers import SongSerializer
from .models import Song


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('title')
    serializer_class = SongSerializer


class SongListView(ListView):
    queryset = Song.objects.all()
    context_object_name = 'songs'
    template_name = 'songs/list.html'


class SongUpdateView(UpdateView):
    model = Song
    fields = ['title', 'author', 'lyrics']
    success_url = "/"
