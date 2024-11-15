from django.db import models
from django.contrib.auth.models import User

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kanji_per_day = models.IntegerField(choices=[(1, '1'), (2, '2'), (5, '5'), (10, '10')], default=5)
    duration_in_days = models.IntegerField(choices=[(7, '7 Days'), (14, '14 Days'), (30, '30 Days'), (60, '60 Days')], default=14)
    email_time = models.TimeField(default="09:00")  # Time of day when the email should be sent
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s Preferences"


