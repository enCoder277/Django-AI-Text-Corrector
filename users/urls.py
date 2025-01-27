from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),      #users:login
    #path('logout/', LogoutView.as_view(), name='logout'),  #users:logout
]