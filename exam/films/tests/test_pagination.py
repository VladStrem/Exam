from datetime import timedelta, date
from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse

from ..models import Movie, Genre


class MoviePaginationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.genre = Genre.objects.create(name="Adventure")
        for i in range(10):
            Movie.objects.create(
                title=f"Test Movie {i}",
                director="Test Director",
                description="Test description",
                release_date=date.today(),
                duration=timedelta(minutes=90),
                genre=self.genre,
                budget=40.0,
                user=self.user
            )

    def test_movie_list_pagination(self):
        response = self.client.get(reverse('films:movies-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['movies'].has_next())
        self.assertEqual(len(response.context['movies']), 3)  # Assuming 3 movies per page
