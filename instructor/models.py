from django.db import models
from users.models import CustomUser

class Instructor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='instructor_profile')
    expertise = models.CharField(max_length=200)
    experience = models.PositiveIntegerField()  
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.name} - {self.course}"