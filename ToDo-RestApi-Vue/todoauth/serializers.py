from .models import *
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    username=models.CharField(max_length=150)
    password = serializers.CharField(max_length=65, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    class Meta:
        model=User
        fields='__all__'    

    # def validate(self,data):
    #     email=data.get("email",""),
    #     password=make_password(data.get("password")),
        
        
        
    #     if User.objects.filter(email=email).exists():
    #         raise exceptions.ValidationError("email is exists")
    #     return super().validate(data)

    # def create(self,validated_data):
    #     return User.objects.create(**validated_data)


    def save(self):
        user = User.objects.create(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            ) 
        password=self.validated_data['password']
        user.set_password(password)
        user.save()
        return user















