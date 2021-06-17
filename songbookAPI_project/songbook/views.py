from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .serializers import SongSerializer
from .models import Song
from .forms import SongModelForm


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all().order_by('title')
    serializer_class = SongSerializer


@method_decorator(login_required, name='dispatch')
class SongListView(ListView):
    queryset = Song.objects.all()
    template_name = 'songbook/song_list.html'
    context_object_name = 'songs'


@method_decorator(login_required, name='dispatch')
class SongCreateView(CreateView):
    queryset = Song.objects.all()
    template_name = 'songbook/song_form.html'
    form_class = SongModelForm


@method_decorator(login_required, name='dispatch')
class SongDetailView(DetailView):
    queryset = Song.objects.all()
    template_name = 'songbook/song_detail.html'
    context_object_name = 'song'


@method_decorator(login_required, name='dispatch')
class SongUpdateView(UpdateView):
    queryset = Song.objects.all()
    template_name = 'songbook/song_form.html'
    form_class = SongModelForm


@method_decorator(login_required, name='dispatch')
class SongDeleteView(DeleteView):
    queryset = Song.objects.all()
    template_name = 'songbook/song_delete.html'
    context_object_name = 'song'

    def get_success_url(self):
        return reverse('song_list')
