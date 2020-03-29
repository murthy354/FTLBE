from django.db import models
from django.contrib.auth.models import User


class Members(models.Model):
    identity = models.CharField(max_length=100)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)



class ActivityPeriods(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    activity_periods = models.ForeignKey(Members, on_delete=models.CASCADE)