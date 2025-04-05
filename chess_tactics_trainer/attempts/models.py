from django.db import models

# Create your models here.

from users.models import CustomUser
from puzzles.models import Puzzle

class Attempt(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    attempted_solution = models.CharField(max_length=100)
    result = models.BooleanField()  # correct/incorrect
