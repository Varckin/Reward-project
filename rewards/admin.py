from django.contrib import admin
from .models import CustomUser, RewardLog, ScheduledReward
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(RewardLog)
admin.site.register(ScheduledReward)
