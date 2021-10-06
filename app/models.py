from django.db import models
from typing import List


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    rating = models.PositiveIntegerField(help_text="1 means bad, 5 means good")

def create_song(title, artist, genre, rating):
    new_song = Song(title=title, artist=artist, genre=genre, rating=rating)
    new_song.save()
    return new_song

def all_songs():
    return Song.objects.all()

def find_song_by_title(title):
    try:
        return Song.objects.get(title=title)
    except Song.DoesNotExist:
        return None

def find_song_by_genre(genre):
    return Song.objects.filter(genre=genre)

def update_song_rating(title, rating):
    song = find_song_by_title(title)
    song.rating = rating
    song.save()

def delete_song(title):
    song = find_song_by_title(title)
    song.delete()
    