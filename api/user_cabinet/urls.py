from django.urls import path
from .views import *


urlpatterns = [
    path('user/update/<int:pk>', UserUpdateView.as_view()),
]