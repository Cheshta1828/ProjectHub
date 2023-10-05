from .models import *

from rest_framework import serializers
class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ('email','password','type')
    def save(self, **kwargs):
        
        return super().save(**kwargs)
    
        
    




class CollegeSpocSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = CollegeSpoc
        fields = '__all__'
        exclude=('is_verified',)