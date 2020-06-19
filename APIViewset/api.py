from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class detailed(APIView):

    def get(self,request):
        model=details.objects.all()
        serializer=detailsSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=detailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

     #def post
     # 
     #def update

class Moredetail(APIView):

    def get(self,request,id):
        model=details.objects.get(id=id)
        serializer=detailsSerializer(model)
        return Response(serializer.data)

    def put(self,request,id):
        model=details.objects.get(id=id)
        serializer=detailsSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    
    def delete(self,request,id):
        model=details.objects.get(id=id)
        model.delete()
        return Response("Successful deteled the data")


    


    


        


    
            


