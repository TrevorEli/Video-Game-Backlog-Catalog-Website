from django.urls import path
from catalog import views
from catalog.models import GameLog


display_list_view = views.DisplayListView.as_view(
    queryset=GameLog.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="game_list",
    template_name="catalog/display_log.html",
)

home_latest_game = views.DisplayListView.as_view(
    queryset=GameLog.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="game_list",
    template_name="catalog/home.html",
)

urlpatterns = [
    path("", home_latest_game, name="home"),
    path("new_game/", views.game_log, name="new_game"),
    path("display/", display_list_view, name="display"),
]

