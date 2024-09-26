from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('', views.movie_list, name='movies-list'),
    path('search/', views.MovieSearchView.as_view(), name='movies-search'),

    path('<int:pk>/', views.MovieDetailView.as_view(), name='movies-detail'),
    path('create/', views.MovieCreateView.as_view(), name='movies-create'),
    path('<int:pk>/update/', views.MovieUpdateView.as_view(), name='movies-update'),
    path('<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movies-delete'),

    path('cards/', views.movie_cards, name='movies-cards'),

    path('genres/', views.GenreListView.as_view(), name='genre-list'),
    path('genres/create/', views.GenreCreateView.as_view(), name='genre-create'),
    path('genres/<int:pk>/edit/', views.GenreUpdateView.as_view(), name='genre-update'),
    path('genres/<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre-delete'),

]
