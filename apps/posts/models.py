from django.db import models
from apps.users.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    image_or_video = models.FileField(
        upload_to='posts_files/'
    )
    description = models.TextField(
        max_length=550
    )
    created = models.DateTimeField(
        auto_now_add=True
    )