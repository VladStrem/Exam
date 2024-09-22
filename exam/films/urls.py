from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movies-list'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movies-detail'),
    path('create/', views.MovieCreateView.as_view(), name='movies-create'),
    path('<int:pk>/update/', views.MovieUpdateView.as_view(), name='movies-update'),
    path('<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movies-delete'),
    path('cards/', views.movie_cards, name='movies-cards')
]
