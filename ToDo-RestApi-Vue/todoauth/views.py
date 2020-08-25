from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from .serializers import *
from rest_framework import status
from rest_framework.generics import GenericAPIView

# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class=UserSerializer
   
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            mname=serializer.save()
            data['response']="successfully registered"
            data['username']=mname.username
            data['first_name']=mname.email
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


