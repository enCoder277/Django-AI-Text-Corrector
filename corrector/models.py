from django.db import models
from django.contrib.auth.models import User

class Correction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_text = models.TextField()
    corrected_text = models.TextField()
    explanation = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Correction by {self.user.username} on {self.timestamp}"