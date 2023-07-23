from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mood(models.Model):
    EMOTIONS = [
    ('JO', 'Joy'),
    ('PE', 'Peace'),
    ('SA', 'Satisfaction'),
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

    INTENSITIES = [
        ('1', 'Barely'),
        ('2', 'Mildly'),
        ('3', 'Moderately'),
        ('4', 'Very'),
        ('5', 'Extremely'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=2, choices=EMOTIONS)
    intensity = models.CharField(max_length=1, choices=INTENSITIES)
    notes = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s mood on {self.timestamp}"

