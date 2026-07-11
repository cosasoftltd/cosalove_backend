from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class DialogueRoom(models.Model):
    user_one = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rooms_as_one')
    user_two = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rooms_as_two')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Prevent a user from being in a room with themselves
        if self.user_one == self.user_two:
            raise ValidationError("A room must have two distinct participants.")

    def __str__(self):
        return f"Dialogue: {self.user_one.username} & {self.user_two.username}"

class Message(models.Model):
    room = models.ForeignKey(DialogueRoom, on_delete=models.CASCADE,related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)