from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

from apps.authentication.serializers import UpdateUserSerializer
from apps.product.serializers import UserSerializer

User = get_user_model()


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UpdateUserSerializer
