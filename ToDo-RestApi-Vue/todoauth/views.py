from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.contrib.auth import login,logout
# Create your views here.

class RegisterView(GenericAPIView):
    serializer_class=UserSerializer
   
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        data={}
        if serializer.is_valid(raise_exception=True):
            mname=serializer.save()
            data['response']="successfully registered"
            data['username']=mname.username
            data['first_name']=mname.email
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class loginView(APIView):

    def post(self,request):
        serializer=loginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.validated_data['user']
            login(request,user)
            token,created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key},status=200)
        return Response("Unable to login retry once ")


class logoutView(APIView):

    def post(self,request):
        logout(request)
        return Response("successfully logged out ")
        
