from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class datalist(APIView):
    def get(self,request):
        model=data.objects.all()
        serializer=dataSerializers(model,many=True)
        return Response(serializer.data)

    def delete(self,request,id):
        model=data.objects.get(id=id)
        model.delete()
        return Response(serializer.data)


class dataDetail(APIView):
    def get(self,request,id):
        model=data.objects.get(id=id)
        serializer=dataSerializers(model)
        return Response(serializer.data)

    def delete(self,request,id):
        model=data.objects.get(id=id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


