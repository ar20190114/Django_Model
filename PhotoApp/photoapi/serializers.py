from dataclasses import fields
from rest_framework import serializers
from .models import PhotoImageModel 

class PhotoImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhotoImageModel
        fields = '__all__'
        