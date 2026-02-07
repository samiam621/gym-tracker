from django.db import models
from django.contrib.auth.models import User


class GymVisit(models.Model):
    """Records when a user went to the gym."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'date']  # One visit per day
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"
