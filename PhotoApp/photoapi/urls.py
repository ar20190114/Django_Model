from django.urls import path, include
from .views import PhotoImageView
from rest_framework import routers
from .views import PhotoImageView

router = routers.SimpleRouter()
router.register(r'User', PhotoImageView)

urlpatterns = [
    path('',include(router.urls)),
]
