from rest_framework import serializers
from .models import Message, Match

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Message
        # Removed 'receiver' - it does not exist in the Message model
        fields = ['id', 'match', 'sender', 'sender_name', 'content', 'timestamp', 'is_read']

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'user_one', 'user_two', 'status', 'matched_at']