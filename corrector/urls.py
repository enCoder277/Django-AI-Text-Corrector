from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path("", correct_text, name="correct_text"),
    path("history/", history, name="history"),
    path("rate/<int:correction_id>/", rate_correction, name="rate_correction"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
]