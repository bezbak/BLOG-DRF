from django.db import models
from apps.users.models import User
# Create your models here.

class Chat(models.Model):
    user_one = models.ForeignKey(
        User,
        related_name='to_chat',
        on_delete=models.CASCADE
    )
    user_two = models.ForeignKey(
        User,
        related_name='from_chat',
        on_delete=models.CASCADE
    )
    
class Message(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='to_message',
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User,
        related_name='from_message',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    chat = models.ForeignKey(
        Chat,
        verbose_name='messages',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )