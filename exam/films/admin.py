from django.contrib import admin
from .models import Movie, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_date', 'genre', 'budget')
    search_fields = ('title', 'director')
    list_filter = ('genre', 'release_date')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
