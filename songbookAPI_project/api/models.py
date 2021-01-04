from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=60)
    lyrics = models.TextField()
    author = models.CharField(max_length=60)

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{} - {}".format(self.author, self.title)
