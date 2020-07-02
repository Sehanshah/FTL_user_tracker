from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user_id = models.CharField(max_length=255)
    real_name = models.CharField(max_length=255)
    tz = models.CharField(max_length=255)

    def __str__(self):
        return self.user_id


class ActivityPeriod(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.user.user_id + " - " + str(self.id)
