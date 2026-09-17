from django.db import models  # type: ignore[reportMissingImports]
from django.contrib.auth.models import User  # type: ignore[reportMissingImports]
from .models import Todo

class TaskAnalytics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Todo, on_delete=models.CASCADE)
    ai_category = models.CharField(max_length=20)
    ai_priority = models.CharField(max_length=10)
    user_accepted_category = models.BooleanField(default=False)
    user_accepted_priority = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Task Analytics"