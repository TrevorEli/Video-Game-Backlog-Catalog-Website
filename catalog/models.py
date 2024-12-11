from django.db import models
from django.utils import timezone

# change name later
class GameLog(models.Model):
    game_title = models.CharField(max_length=300)
    year_released = models.IntegerField(default=0)
    console = models.CharField(max_length=100, default='0000000')

    class PlayDegree(models.IntegerChoices):
        NOT_MUCH = 1
        SOME_WHAT = 2
        WANTS_TO = 3
        VERY_MUCH = 4

    want_to_play_degree = models.IntegerField(choices=PlayDegree, default=1)

    # Gonna keep this
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.game_title}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

