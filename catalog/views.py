import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from catalog.forms import GameLogForm
from catalog.models import GameLog
from django.views.generic import ListView


# Remove the old home function if you want; it's no longer used

class DisplayListView(ListView):
    """Renders the list, with a list of all messages."""
    model = GameLog

    def get_context_data(self, **kwargs):
        context = super(DisplayListView, self).get_context_data(**kwargs)
        return context



def game_log(request):
    form = GameLogForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            game_title = form.save(commit=False)
            game_title.log_date = datetime.now()
            game_title.save()

            return redirect("home")
    else:
        return render(request, "catalog/game_log.html", {"form": form})

def home(request):
    return render(request, "catalog/home.html")

"""def display_log(request):
    
    #return render(request, "catalog/display_log.html")"""
