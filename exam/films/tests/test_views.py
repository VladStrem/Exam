from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Genre, Movie
from datetime import timedelta, date


class MovieViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.genre = Genre.objects.create(name="Drama")
        self.movie = Movie.objects.create(
            title="Test Movie",
            director="Test Director",
            description="Test description",
            release_date=date.today(),
            duration=timedelta(minutes=120),
            genre=self.genre,
            budget=60.0,
            user=self.user
        )

    def test_movie_list_view(self):
        response = self.client.get(reverse('films:movies-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)

    def test_movie_detail_view(self):
        response = self.client.get(reverse('films:movies-detail', args=[self.movie.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)

    def test_movie_create_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse('films:movies-create'), {
            'title': 'New Movie',
            'director': 'New Director',
            'description': 'New description',
            'release_date': date.today(),
            'genre': self.genre.pk,
            'budget': 70.0,
            'duration_in_minutes': 140
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation


class GenreViewTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Thriller")

    def test_genre_list_view(self):
        response = self.client.get(reverse('films:genre-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.genre.name)

    def test_genre_create_view(self):
        response = self.client.post(reverse('films:genre-create'), {'name': 'Sci-Fi'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Genre.objects.filter(name='Sci-Fi').exists())
