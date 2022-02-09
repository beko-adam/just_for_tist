from rest_framework import routers, serializers, viewsets
from .models import *


# Serializers define the API representation.


class Cuo_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Customer
        fields = '__all__'




class Pro_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'




class Tag_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'