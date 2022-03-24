from django.db import models
from django.utils import timezone
from django.urls import reverse


class Song(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    lyrics = models.TextField()

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} - {}".format(self.author, self.title)

    def get_absolute_url(self):
        return reverse('song_detail', args=[self.id])
