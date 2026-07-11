from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Dossier

User = get_user_model()

class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dossier
        fields = [
            'id', 'name', 'birthdate', 'avatar_url', 'bio', 
            'archetype', 'traits', 'philosophy', 'value_system', 'lifestyle'
        ]

class ProfileSerializer(serializers.ModelSerializer):
    # Mapping fields from the related Dossier model
    archetype = serializers.CharField(source="dossier.archetype", read_only=True)
    traits = serializers.JSONField(source='dossier.traits', read_only=True)
    age = serializers.IntegerField(source='dossier.age', read_only=True)
    bio = serializers.CharField(source='dossier.bio', read_only=True)
    philosophy = serializers.CharField(source='dossier.philosophy', read_only=True)
    valueSystem = serializers.CharField(source='dossier.value_system', read_only=True)
    lifestyle = serializers.CharField(source='dossier.lifestyle', read_only=True)
    
    # Custom field for the avatar URL
    avatarUrl = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'age', 'archetype', 'avatarUrl', 
            'traits', 'bio', 'philosophy', 'valueSystem', 'lifestyle'
        ]

    def get_avatarUrl(self, obj):
        request = self.context.get('request')
        # Check if the user has a dossier AND has an avatar image
        if hasattr(obj, 'dossier') and obj.dossier and obj.dossier.avatar_url:
            if request:
                return request.build_absolute_uri(obj.dossier.avatar_url.url)
            return obj.dossier.avatar_url.url
        return None