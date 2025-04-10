from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import status
from .models import RewardLog, ScheduledReward
from .tasks import process_scheduled_reward
from datetime import timedelta

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'coins': user.coins
        })

class RewardListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rewards = RewardLog.objects.filter(user=request.user)
        return Response([
            {'amount': r.amount, 'given_at': r.given_at} for r in rewards
        ])

class RewardRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        now = timezone.now()
        if ScheduledReward.objects.filter(user=user, execute_at__gt=now - timedelta(days=1)).exists():
            return Response({'detail': 'Reward already requested today'}, status=400)
        
        reward = ScheduledReward.objects.create(
            user=user, amount=10, execute_at=now + timedelta(minutes=5)
        )
        process_scheduled_reward.apply_async((reward.id,), eta=reward.execute_at)
        return Response({'detail': 'Reward scheduled'})
