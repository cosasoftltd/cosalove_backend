import random
from datetime import date
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Dossier, DiscoveryExposure
from .serializers import DossierSerializer, ProfileSerializer

User = get_user_model()

# --- EXISTING DOSSIER VIEWS ---

class DossierDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dossier = Dossier.objects.get(user=request.user)
        serializer = DossierSerializer(dossier)
        return Response(serializer.data)

class DossierCalibrationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        dossier = Dossier.objects.get(user=request.user)
        serializer = DossierSerializer(dossier, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Calibration complete", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- PERSISTENT DISCOVERY FEED ---

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_discovery_feed(request):
    # 1. Generate a seed
    today_seed = int(date.today().strftime("%Y%m%d"))
    random.seed(today_seed + request.user.id)
    
    # 2. Get all other users, excluding the current user AND the admin
    # Exclude 'admin' by username (or use .exclude(is_staff=True) if applicable)
    candidates = list(User.objects.exclude(id=request.user.id).exclude(username='Khanda'))
    
    # 3. Shuffle using our daily seed
    random.shuffle(candidates)
    
    # 4. Take the top 10
    daily_matches = candidates[:10]
    
    # 5. Serialize
    serializer = ProfileSerializer(daily_matches, many=True, context={'request': request})
    
    return Response(serializer.data)


# --- OPTIONAL: SWIPE ACTION ---
# Use this if you want to track which ones the user explicitly 'passed' or 'liked'
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def record_swipe(request):
    target_id = request.data.get('target_id')
    # You can add logic here to mark users as "seen" in your database
    # if you want to remove them after a user takes an action.
    return Response({"status": "action recorded"})