from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .forms import MovieForm
from .models import Movie


def movie_cards(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {'movies': movies})


class MovieListView(ListView):
    model = Movie
    template_name = 'films/movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Movie.objects.filter(
                Q(title__icontains=query) | Q(director__icontains=query)
            ).select_related('genre')
        return Movie.objects.select_related('genre')


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'films/movies/movie_detail.html'


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'films/movies/movie_form.html'
    success_url = reverse_lazy('films:movies-list')


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'films/movies/movie_form.html'
    success_url = reverse_lazy('films:movies-list')


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'films/movies/movie_confirm_delete.html'
    success_url = reverse_lazy('films:movies-list')
