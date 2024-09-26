from django.test import TestCase
from ..forms import MovieForm, GenreForm
from ..models import Genre
from datetime import date


class GenreFormTest(TestCase):
    def test_genre_form_valid(self):
        form = GenreForm(data={'name': 'Horror'})
        self.assertTrue(form.is_valid())

    def test_genre_form_invalid(self):
        form = GenreForm(data={})
        self.assertFalse(form.is_valid())


class MovieFormTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Action")

    def test_movie_form_valid(self):
        form_data = {
            'title': 'Test Movie',
            'director': 'Test Director',
            'description': 'Test description',
            'release_date': date.today(),
            'genre': self.genre.pk,
            'budget': 50.0,
            'duration_in_minutes': 120
        }
        form = MovieForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_movie_form_invalid(self):
        form_data = {
            'title': '',  # Empty title
            'director': 'Test Director',
            'description': 'Test description',
            'release_date': date.today(),
            'genre': self.genre.pk,
            'budget': 50.0,
            'duration_in_minutes': 120
        }
        form = MovieForm(data=form_data)
        self.assertFalse(form.is_valid())
