from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import ImageSerializer, MemberSerializer
from .models import Image, Member
import json

# Create your views here.


class GetImageViewSet(generics.ListAPIView):

    '''Add and Get Images'''

    queryset = Image.objects.all()
    serializer_class = ImageSerializer


    def post(self, request, m_id):
        member = Member.objects.get(id=m_id)  
        image_post = Image(member_id=member)
        serializer = ImageSerializer(image_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)

       
    def get(self, request, m_id):
    
        all_images = Image.objects.filter(member_id=m_id)
        image_serializer = ImageSerializer(all_images, many=True)

        member = Member.objects.filter(id=m_id)
        member_serializer = MemberSerializer(member, many=True) 
        return JsonResponse({
                            'user_id': member_serializer.data[0]['id'],
                            'user_name':member_serializer.data[0]['name'],
                            'image': image_serializer.data
                            }, safe=False)
      


class MemberViewSet(generics.ListAPIView):

    ''' Creat and Get member'''

    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        name = request.data['name']
        image = Member.objects.create(name=name)
        return HttpResponse(image, status=200)

    def get(self, request):
        all_members = Member.objects.all()
        member_serializer = MemberSerializer(all_members, many=True)

        return JsonResponse(member_serializer.data, safe=False)


