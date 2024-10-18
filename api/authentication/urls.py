from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserCreateView.as_view()),
    path('auth/', NewAuthView.as_view(), name='token_obtain_pair'),
]
