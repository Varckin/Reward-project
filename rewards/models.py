from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    coins = models.IntegerField(default=0)

class ScheduledReward(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.IntegerField()
    execute_at = models.DateTimeField()

class RewardLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.IntegerField()
    given_at = models.DateTimeField(auto_now_add=True)
