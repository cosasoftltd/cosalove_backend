from django.db import models
from django.conf import settings

# Create your models here.
class Match(models.Model):
    user_one = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_one')
    user_two = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_two')
    status = models.CharField(max_length=255, default='pending')
    matched_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    # Linking to the Match object ensures the message belongs to a specific conversation
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='messages')
    
    # The user who sent the message
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    
    # The content of the conversation
    content = models.TextField()
    
    # Tracking status
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"