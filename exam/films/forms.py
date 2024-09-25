# from django import forms
# from .models import Movie
#
#
# class MovieForm(forms.ModelForm):
#     class Meta:
#         model = Movie
#         fields = ['title', 'director', 'description', 'release_date', 'duration', 'genre', 'budget', 'poster']

from django import forms
from .models import Movie, Genre
from django.forms.widgets import DateInput
from datetime import timedelta


class MovieForm(forms.ModelForm):
    duration_in_minutes = forms.IntegerField(
        min_value=1,  # Мінімальне значення для тривалості фільму в хвилинах
        label="Duration (minutes)",
        help_text="Enter the duration in minutes"
    )

    class Meta:
        model = Movie
        fields = ['title', 'director', 'description', 'release_date', 'genre', 'budget', 'poster']
        widgets = {
            'release_date': DateInput(attrs={'type': 'date'}),  # Календарик для дати
        }

    def save(self, commit=True):
        # Конвертуємо хвилини в timedelta перед збереженням
        movie = super().save(commit=False)
        minutes = self.cleaned_data['duration_in_minutes']
        movie.duration = timedelta(minutes=minutes)

        if commit:
            movie.save()

        return movie

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.duration:
            # Ініціалізуємо поле duration_in_minutes значенням з бази даних
            self.fields['duration_in_minutes'].initial = int(self.instance.duration.total_seconds() // 60)


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter genre name'}
            )
        }
