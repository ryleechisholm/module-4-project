from django.test import TestCase
from app import models

class TestSong(TestCase):
    def test_can_create_song(self):
        song = models.create_song(
            "Party in the USA",
            "Miley Cyrus",
            "Pop",
            5,
        )
        self.assertEqual(song.id, 1)
        self.assertEqual(song.title, "Party in the USA")
        self.assertEqual(song.artist, "Miley Cyrus")
        self.assertEqual(song.genre, "Pop")
        self.assertEqual(song.rating, 5)
    def test_can_view_all_songs_at_once(self):
        songs_data = [
            {
                "title": "Radioactive",
                "artist": "Imagine Dragons",
                "genre": "Alternative",
                "rating": 5,
            },
            {
                "title": "Never Gonna Give You Up",
                "artist": "Rick Astley",
                "genre": "Pop",
                "rating": 2,
            },
            {
                "title": "Somebody to Love",
                "artist": "Queen",
                "genre": "Pop",
                "rating": 4,
            },
        ]
        for song_data in songs_data:
            models.create_song(
                song_data["title"],
                song_data["artist"],
                song_data["genre"],
                song_data["rating"],
            )
        songs = models.all_songs()
        self.assertEqual(len(songs), len(songs_data))
        songs_data = sorted(songs_data, key=lambda c: c["title"])
        songs = sorted(songs, key=lambda c: c.title)
        for data, song in zip(songs_data, songs):
            self.assertEqual(data["title"], song.title)
            self.assertEqual(data["artist"], song.artist)
            self.assertEqual(data["genre"], song.genre)
            self.assertEqual(data["rating"], song.rating)
    def test_can_search_by_title(self):
        songs_data = [
            {
                "title": "Radioactive",
                "artist": "Imagine Dragons",
                "genre": "Alternative",
                "rating": 5,
            },
            {
                "title": "Never Gonna Give You Up",
                "artist": "Rick Astley",
                "genre": "Pop",
                "rating": 2,
            },
            {
                "title": "Somebody to Love",
                "artist": "Queen",
                "genre": "Pop",
                "rating": 4,
            },
        ]
        for song_data in songs_data:
            models.create_song(
                song_data["title"],
                song_data["artist"],
                song_data["genre"],
                song_data["rating"],
            )
        self.assertIsNone(models.find_song_by_title("aousnth"))
        song = models.find_song_by_title("Somebody to Love")
        self.assertIsNotNone(song)
        self.assertEqual(song.artist, "Queen")
    def test_can_view_genre(self):
        songs_data = [
            {
                "title": "Radioactive",
                "artist": "Imagine Dragons",
                "genre": "Alternative",
                "rating": 5,
            },
            {
                "title": "Never Gonna Give You Up",
                "artist": "Rick Astley",
                "genre": "Pop",
                "rating": 2,
            },
            {
                "title": "Somebody to Love",
                "artist": "Queen",
                "genre": "Pop",
                "rating": 4,
            },
        ]
        for song_data in songs_data:
            models.create_song(
                song_data["title"],
                song_data["artist"],
                song_data["genre"],
                song_data["rating"],
            )
        self.assertEqual(len(models.find_song_by_genre(genre="Pop")), 2)
    def test_can_update_rating(self):
        songs_data = [
            {
                "title": "Radioactive",
                "artist": "Imagine Dragons",
                "genre": "Alternative",
                "rating": 5,
            },
            {
                "title": "Never Gonna Give You Up",
                "artist": "Rick Astley",
                "genre": "Pop",
                "rating": 2,
            },
            {
                "title": "Somebody to Love",
                "artist": "Queen",
                "genre": "Pop",
                "rating": 4,
            },
        ]
        for song_data in songs_data:
            models.create_song(
                song_data["title"],
                song_data["artist"],
                song_data["genre"],
                song_data["rating"],
            )
        models.update_song_rating("Never Gonna Give You Up", 4)
        self.assertEqual(
            models.find_song_by_title("Never Gonna Give You Up").rating, 4
        )
    def test_can_delete_song(self):
        songs_data = [
            {
                "title": "Radioactive",
                "artist": "Imagine Dragons",
                "genre": "Alternative",
                "rating": 5,
            },
            {
                "title": "Never Gonna Give You Up",
                "artist": "Rick Astley",
                "genre": "Pop",
                "rating": 2,
            },
            {
                "title": "Somebody to Love",
                "artist": "Queen",
                "genre": "Pop",
                "rating": 4,
            },
        ]
        for song_data in songs_data:
            models.create_song(
                song_data["title"],
                song_data["artist"],
                song_data["genre"],
                song_data["rating"],
            )
        models.delete_song("Somebody to Love")
        self.assertEqual(len(models.all_songs()), 2)
