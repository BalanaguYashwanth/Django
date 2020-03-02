from rest_framework import routers, serializers, viewsets

from todo.models import data
class dataSerializers(serializers.ModelSerializer):
    class Meta:
        model = data
        fields = '__all__'
        