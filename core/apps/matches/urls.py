from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, MessageViewSet
from django.urls import path, include

router = DefaultRouter()
# This registers /api/matches/matches/
router.register(r'matches', MatchViewSet, basename='match')
# This registers /api/matches/messages/
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]