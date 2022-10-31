from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()

    
    def __str__(self):
        return self.first_name

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    title = models.CharField(max_length=250)
    date_released = models.DateField(auto_now=False)
    likes = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    


class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
    content = models.TextField(max_length=20000)

    
    def __str__(self):
        return self.content[:5]
