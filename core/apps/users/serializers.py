from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email') # Ensure these match what you send
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # IMPORTANT: Use create_user so the password gets hashed!
        user = User.objects.create_user(**validated_data)
        return user