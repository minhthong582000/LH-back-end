from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import authentication
from userprofile.models import User
from rest_framework.response import Response

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'password', 
            'name', 
            'email', 
            'is_teacher', 
            'about_me', 
            'gender',
            'user_type',
            'credit',
            ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            name=validated_data["name"],
            email=validated_data["email"],
            is_teacher=validated_data["is_teacher"],
            about_me=validated_data["about_me"],
            gender=validated_data["gender"],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")