from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'author', 'lyrics', 'pub_date')
