from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'description', 'release_date', 'duration', 'genre', 'budget', 'poster']
