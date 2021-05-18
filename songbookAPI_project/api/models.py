from django.db import models
from django.utils import timezone
from django.urls import reverse


class Song(models.Model):
    title = models.CharField(max_length=60)
    lyrics = models.TextField()
    author = models.CharField(max_length=60)

    pub_date = models.DateTimeField(default=timezone.now)

    # def get_absolute_url(self):
    #     return reverse('song_editor', args=[self.id])

    def __str__(self):
        return "{} - {}".format(self.author, self.title)
