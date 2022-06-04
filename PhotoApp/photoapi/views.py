from django.shortcuts import render
from django.views import generic
from .forms import PhotoImageForm
from .models import PhotoImageModel
import shutil
import os
from rest_framework import viewsets
from .serializers import PhotoImageSerializers


class PhotoImageView(viewsets.ModelViewSet):
    form_class = PhotoImageForm
    queryset = PhotoImageModel.objects.all()
    serializer_class = PhotoImageSerializers


    # postメソッドをオーバーライドする
    def post(self, request):
        form = PhotoImageForm(request.POST)

        sample = PhotoImageModel()
        sample.img = request.FILES['img']
        sample.save()
        sample_img = sample.img

        #人工知能プログラムを使って犬か猫を判定するru
        from .photoimage import Dogorcat
        img = request.FILES['img']
        dog, cat = Dogorcat(img)

        return render(request, self.template_name, {
            'dog': self.dog, 'cat': cat,
        }
                    )
