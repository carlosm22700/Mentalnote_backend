from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Define Mood model
class Mood(models.Model):

    #define choices for emotion field
    EMOTIONS = [
        ('JO', 'Joy'),
        ('PE', 'Peace'),
        ('ST', 'Satisfaction'),
        ('HO', 'Hope'),
        ('CO', 'Courage'),
        ('BO', 'Boredom'),
        ('FR', 'Frustration'),
        ('AN', 'Anxiety'),
        ('SA', 'Sadness'),
        ('AN', 'Anger'),
        ('FE', 'Fear'),
        ('DE', 'Despair'),
    ]

    #define choices for the intensity field
    INTENSITIES = [
        ('1', 'Barely'),
        ('2', 'Mildly'),
        ('3', 'Moderately'),
        ('4', 'Very'),
        ('5', 'Extremely'),
    ]

    #define a FK field. Establishes manty-to-one reltationship with User. Each user can have many moods
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Define a CharField for 'emotion' and 'intensity'. max_length is required, and choices restricts the possible values to those defined in EMOTIONS/INTENSITIES.
    emotion = models.CharField(max_length=2, choices=EMOTIONS)
    intensity = models.CharField(max_length=1, choices=INTENSITIES)
    #define TextField for 'notes'
    notes = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    #define the string representation of a Mood object.
    def __str__(self):
        return f"{self.user}'s mood on {self.timestamp}"

