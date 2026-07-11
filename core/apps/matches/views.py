from rest_framework import viewsets, permissions
from .models import Match, Message
from .serializers import MatchSerializer, MessageSerializer
from django.db.models import Q

class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Match.objects.filter(
            Q(user_one=self.request.user) | Q(user_two=self.request.user)
        ).order_by('-matched_at')

class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Correctly filters messages belonging to any match involving the current user
        return Message.objects.filter(
            Q(match__user_one=self.request.user) | Q(match__user_two=self.request.user)
        ).distinct().order_by('-timestamp')