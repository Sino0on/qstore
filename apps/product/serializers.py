from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'mailings', 'date_of_birth', 'gender']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            mailings=validated_data['mailings'],
            date_of_birth=validated_data['date_of_birth'],
            gender=validated_data['gender']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ListProductSerializer(serializers.Serializer):
    goods = serializers.JSONField()

    def create(self, validated_data):
        for i in validated_data['das']:
            print(i)
        return {'Привет': 'Привет'}