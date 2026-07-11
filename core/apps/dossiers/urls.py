from django.urls import path
from .views import DossierCalibrationView,DossierDetailView, get_discovery_feed

urlpatterns = [
    path('profile/', DossierDetailView.as_view(), name='dossier-detail'),
    path('calibrate/', DossierCalibrationView.as_view(), name='dossier-calibrate'),
    path('matches/', get_discovery_feed,name="discovery-matches"),
]