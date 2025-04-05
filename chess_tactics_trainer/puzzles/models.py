from django.db import models

# Create your models here.

class Puzzle(models.Model):
    difficulty_level = models.CharField(max_length=10)
    chess_position = models.CharField(max_length=100)  # FEN string
    solution = models.CharField(max_length=100)
