from rest_framework import generics
from .models import User, Mood
from .serializers import UserSerializer, MoodSerializer

# Define a view for a list of User objects. This view can be used to get a list of all users or to create a new user.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all() # Get all user objects
    serializer_class = UserSerializer

# Define a view for a list of Mood objects. This view can be used to get a list of all users or to create a new user.
class MoodList(generics.ListCreateAPIView):
    queryset = Mood.objects.all() # Get all mood objects
    serializer_class = MoodSerializer
