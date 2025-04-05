
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from.models import Puzzle
from .forms import PuzzleAttemptForm



def puzzle_list(request):
    puzzles = Puzzle.objects.all()
    return render(request, 'puzzles/puzzle_list.html', {'puzzles': puzzles})


def puzzle_detail(request, puzzle_id):
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id)
    return render(request, 'puzzles/puzzle_detail.html', {'puzzle': puzzle})


def attempt_puzzle(request, puzzle_id):
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id)
    if request.method == 'POST':
        form = PuzzleAttemptForm(request.POST)
        if form.is_valid():
            attempt = form.save(commit=False)
            attempt.puzzle = puzzle
            attempt.save()
            return redirect('puzzle_detail', puzzle_id=puzzle_id)
    else:
        form = PuzzleAttemptForm()
    return render(request, 'puzzles/attempt_puzzle.html', {'puzzle': puzzle, 'form': form})