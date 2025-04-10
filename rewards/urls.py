from django.urls import path
from .views import UserProfileView, RewardListView, RewardRequestView

urlpatterns = [
    path('profile/', UserProfileView.as_view()),
    path('rewards/', RewardListView.as_view()),
    path('rewards/request/', RewardRequestView.as_view()),
]
