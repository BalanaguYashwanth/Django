from rest_framework.views import APIView
from .serializer import *
from todo.models import *
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.contrib.auth.models import User

class todo_api(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)  #main permission 

    def get(self,request):
        model=todo_data.objects.all()
        serializer=todo_dataSerializer(model,many=True) 
        return Response(serializer.data)

    def post(self,request):
        serializer=todo_dataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        model=todo_data.objects.get(id=id)
        model.delete()
        return Response('successfully deleted')


class todo_api_one(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)  #main permission 

    def get(self,request,id):
        model=todo_data.objects.get(id=id)
        serializer=todo_dataSerializer(model)
        return Response(serializer.data)

    def put(self,request,id):
        model=todo_data.objects.get(id=id)
        serializer=todo_dataSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        model=todo_data.objects.get(id=id)
        model.delete()
        return Response('successfully deleted')


class loginView(APIView):
  pass


class logoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self,request):
        logout(request)
        return Response("logout",status=204)


            
        





    

