from rest_framework import serializers
from .models import User, Mood

# Define a serializer for the User model. The Meta class defines what model it applies to and which fields to include.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Define a serializer for the Mood model. The Meta class defines what model it applies to and which fields to include.
class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ('id', 'user', 'emotion', 'intensity', 'notes', 'timestamp')
