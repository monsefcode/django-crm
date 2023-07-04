from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('developer', 'Developer'),
        ('client', 'Client'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username + ' ' + 'Profile'
    
    # Override the save method to resize the image before saving
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # resize image
        img = Image.open(self.image.path)
        
        # resize if image is larger than 300px
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)