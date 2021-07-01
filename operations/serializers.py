from rest_framework import serializers
from .models import Image
from .models import Member

class MemberSerializer(serializers.ModelSerializer):    

    class Meta:        
        model = Member        
        fields = ('id','name')

class ImageSerializer(serializers.ModelSerializer):  
    member = MemberSerializer(many=True,read_only=True)
   
    class Meta:        
        model = Image        
        fields = ('member_id','type','member','image')


