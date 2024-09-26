from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.DurationField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    poster = models.ImageField(upload_to='films/images',
                               default="default.png", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
