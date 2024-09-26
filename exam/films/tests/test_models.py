from django.test import TestCase

from django.contrib.auth.models import User
from datetime import timedelta, date

from ..models import Genre, Movie


class GenreModelTest(TestCase):
    def test_genre_creation(self):
        genre = Genre.objects.create(name="Action")
        self.assertEqual(str(genre), genre.name)


class MovieModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.genre = Genre.objects.create(name="Comedy")

    def test_movie_creation(self):
        movie = Movie.objects.create(
            title="Test Movie",
            director="Test Director",
            description="Test description",
            release_date=date.today(),
            duration=timedelta(minutes=120),
            genre=self.genre,
            budget=50.0,
            user=self.user
        )
        self.assertEqual(str(movie), movie.title)
        self.assertEqual(movie.duration, timedelta(minutes=120))
        self.assertEqual(movie.user, self.user)
