from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.product.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class NewAuthView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.validated_data)
            user = User.objects.get(username=request.data['username'])
            serializer.validated_data['user'] = UserSerializer(user).data

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
