from django import forms

from .models import Song


class SongModelForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'author', 'lyrics']
