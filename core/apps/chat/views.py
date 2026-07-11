from rest_framework import viewsets, permissions
from .models import DialogueRoom
from .serializers import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DialogueRoom.objects.filter(user_one=self.request.user) | \
            DialogueRoom.objects.filter(user_two=self.request.user)
    