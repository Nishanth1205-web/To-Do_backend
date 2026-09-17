from django.db import models  # pyright: ignore[reportMissingModuleSource]

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    # AI-generated fields
    ai_category = models.CharField(max_length=20, blank=True, null=True)
    ai_priority = models.CharField(max_length=10, blank=True, null=True)
    ai_confidence = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.title