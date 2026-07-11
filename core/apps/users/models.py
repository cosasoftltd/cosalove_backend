from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# 1. The Custom User Model
class CustomUser(AbstractUser):
    # You can add fields like birth_date, location, or is_premium here later
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

# 2. The Auto-Creation Signal
# This ensures that whenever a new user is created, a Dossier is born with them.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_dossier_for_new_user(sender, instance, created, **kwargs):
    # We delay this import to avoid circular dependency issues
    from apps.dossiers.models import Dossier
    
    if created:
        Dossier.objects.create(user=instance)