from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    profile_images = models.ImageField(upload_to='profile_images/', blank=True)

    class Meta:
        permissions = [
            ('special status', 'can read profile')
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = None

    def get_absolute_url(self):
        return reverse('profiles:profile_detail', args=[str(self.id)])
