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
    def __str__(self):
        return f"{self.user.username}-Пост-{self.id}"
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        

class Comment(models.Model):
    text = models.CharField(
        max_length=550
    )
    parent = models.ForeignKey(
        'self',
        related_name = 'child_comm',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    from_user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE
    )
    to_post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"{self.text[:10]} - {self.from_user.username}"
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарийи'