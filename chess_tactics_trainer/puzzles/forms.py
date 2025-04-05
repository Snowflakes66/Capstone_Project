from django import forms
from .models import PuzzleAttempt

class PuzzleAttemptForm(forms.ModelForm):
    class Meta:
        model = PuzzleAttempt
        fields = ('move',)
