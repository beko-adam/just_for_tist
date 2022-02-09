from .Serializers import Pro_Serializer, Cuo_Serializer, Tag_Serializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import *



@api_view(['GET'])
def Tag_list(request):

    all_list =  Tag.objects.all()
    data = Tag_Serializer(all_list, many=True).data

    return Response( {'data':data})


@api_view(['GET'])
def Pro_list(request):

    all_list =  Product.objects.all()
    data = Pro_Serializer(all_list, many=True).data

    return Response( {'data':data})


@api_view(['GET'])
def single_pord(request, id):

    single_cous = Product.objects.get(id=id)
    data = Pro_Serializer(single_cous).data

    return Response( {'data':data})


# class generics view  api 
class Por_list_generics(generics.CreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = Pro_Serializer


# class generics view  api 
class Por_list_genericsCRUD(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = Pro_Serializer
    lookup_field = 'id'