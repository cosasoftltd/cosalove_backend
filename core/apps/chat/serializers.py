from rest_framework import serializers
from .models import DialogueRoom, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','room','sender','content','timestamp']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = DialogueRoom
        fields = ['id','user_one','user_two','created_at']

        