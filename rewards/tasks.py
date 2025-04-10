from celery import shared_task
from django.utils import timezone
from .models import ScheduledReward, RewardLog

@shared_task
def process_scheduled_reward(reward_id):
    try:
        reward = ScheduledReward.objects.get(id=reward_id)
        user = reward.user
        user.coins += reward.amount
        user.save()
        RewardLog.objects.create(user=user, amount=reward.amount)
        reward.delete()
    except ScheduledReward.DoesNotExist:
        pass
