from django.urls import path
from .views import MoodList, register, login

urlpatterns = [
    path('moodlogs/', MoodList.as_view(), name='moodlogs'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
