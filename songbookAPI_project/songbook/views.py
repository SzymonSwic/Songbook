from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse

from .serializers import SongSerializer
from .models import Song
from .forms import SongModelForm


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all().order_by('title')
    serializer_class = SongSerializer


class SongListView(ListView):
    queryset = Song.objects.all()
    template_name = 'songs/song_list.html'
    context_object_name = 'songs'


class SongCreateView(CreateView):
    queryset = Song.objects.all()
    template_name = 'songs/song_form.html'
    form_class = SongModelForm


class SongDetailView(DetailView):
    queryset = Song.objects.all()
    template_name = 'songs/song_detail.html'
    context_object_name = 'song'


class SongUpdateView(UpdateView):
    queryset = Song.objects.all()
    template_name = 'songs/song_form.html'
    form_class = SongModelForm


class SongDeleteView(DeleteView):
    queryset = Song.objects.all()
    template_name = 'songs/song_delete.html'
    context_object_name = 'song'

    def get_success_url(self):
        return reverse('song_list')
