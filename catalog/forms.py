from django import forms
from catalog.models import GameLog

class GameLogForm(forms.ModelForm):
    class Meta:
        model = GameLog
        fields = ("game_title", "year_released",)   # NOTE: the trailing comma is required