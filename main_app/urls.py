from django.urls import path
from .views import MoodList

urlpatterns = [
    path('moodlogs/', MoodList.as_view()),
]