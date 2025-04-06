from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
