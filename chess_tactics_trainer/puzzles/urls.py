from django.urls import path
from . import views

urlpatterns = [
    path('puzzles/', views.puzzle_list, name='puzzle_list'),
    path('puzzles/<int:puzzle_id>/', views.puzzle_detail, name='puzzle_detail'),
    path('puzzles/<int:puzzle_id>/attempt/', views.attempt_puzzle, name='attempt_puzzle'),

]

