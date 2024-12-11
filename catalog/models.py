from django.db import models
from django.utils import timezone

# change name later
class GameLog(models.Model):
    game_title = models.CharField(max_length=300)
    year_released = models.IntegerField(default=0)
    # Gonna keep this
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.game_title}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

