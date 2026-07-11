from django.db import models
from django.conf import settings
from datetime import date

class Dossier(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="User")
    birthdate = models.DateField(null=True, blank=True)
    avatar_url = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    # Core Persona
    archetype = models.CharField(max_length=50, blank=True)
    traits = models.JSONField(default=list) # Frontend expects a list
    
    # Detailed Bio Sections
    bio = models.TextField(blank=True)        # Maps to Philosophy/Intro
    philosophy = models.CharField(blank=True, max_length=255)
    value_system = models.TextField(blank=True) # Matches DossierVitals
    lifestyle = models.TextField(blank=True)    # Matches DossierVitals
    
    # Metadata
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    maxDistance = models.BigIntegerField(blank=True, null=True)

    @property
    def age(self):
        if not self.birthdate:
            return None
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

    def __str__(self):
        return self.user.username

class DiscoveryExposure(models.Model):
    viewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='viewing_exposures')
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='targeted_exposures')
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['viewer', 'viewed_at'])]