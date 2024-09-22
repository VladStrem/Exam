from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .forms import MovieForm
from .models import Movie


def movie_cards(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {'movies': movies})


# class MovieListView(ListView):
#     model = Movie
#     template_name = 'films/movies/movie_list.html'
#     context_object_name = 'movies'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if query:
#             movies = Movie.objects.filter(
#                 Q(title__icontains=query) | Q(director__icontains=query)
#             ).select_related('genre')
#             print(f"Filtered movies: {movies.count()}")  # Додайте це для перевірки
#             return movies
#         return Movie.objects.select_related('genre')


def movie_list(request):
    movie_list = Movie.objects.all()
    paginator = Paginator(movie_list, 2)  # По 9 фільмів на сторінці
    page = request.GET.get('page')

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(request, 'films/movies/movie_list.html', {'movies': movies})



class MovieDetailView(DetailView):
    model = Movie
    template_name = 'films/movies/movie_detail.html'


# class MovieCreateView(CreateView):
#     model = Movie
#     fields = ['title', 'description', 'director', 'release_date', 'poster', 'genre']
#     template_name = 'films/movies/movie_form.html'
#
#     def form_valid(self, form):
#         movie = form.save()
#         messages.success(self.request, f"Movie {movie.title} added successfully!")
#         return redirect(reverse('films:movies-list'))


# class MovieUpdateView(UpdateView):
#     model = Movie
#     fields = ['title', 'description', 'director', 'release_date', 'poster', 'genre']
#     template_name = 'films/movies/movie_form.html'
#
#     def form_valid(self, form):
#         messages.success(self.request, "Movie updated successfully!")
#         return redirect(reverse('films:movies-list'))


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'films/movies/movie_form.html'

    # success_url = reverse_lazy('films:movies-list')

    def form_valid(self, form):
        movie = form.save()
        messages.success(self.request, f"Movie {movie.title} added successfully!")
        return redirect(reverse('films:movies-list'))


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'films/movies/movie_form.html'

    # success_url = reverse_lazy('films:movies-list')

    def form_valid(self, form):
        movie = form.save()
        messages.success(self.request, f"Movie {movie.title} updated successfully!")
        return redirect(reverse('films:movies-list'))


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'films/movies/movie_confirm_delete.html'
    success_url = reverse_lazy('films:movies-list')
