from django.shortcuts import render
from rest_framework import viewsets
from .models import RandomModel
from .serializers import RandomModelSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class RandomModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RandomModel.objects.all()
    serializer_class = RandomModelSerializer

