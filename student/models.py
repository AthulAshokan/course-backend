from django.db import models
from users.models import CustomUser

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    image = models.CharField(max_length=200)
    alternative_phone = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return f"{self.user.name} - {self.course}"
