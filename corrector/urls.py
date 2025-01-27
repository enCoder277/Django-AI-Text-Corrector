from django.urls import path
from .views import *

urlpatterns = [
    path('', TextCorrectionView.as_view(), name='correct_text'),
    path('history/', history, name='history'),
    path('rate/<int:correction_id>/', rate_correction, name='rate_correction'),
]