from django.db import models
from core.models import Profile


# Project model
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    client = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name='projects', 
        default=None,
        limit_choices_to={'user_type': 'client'}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    release_date = models.DateTimeField()

    def __str__(self):
        return self.name + ' ' + 'Project' 

