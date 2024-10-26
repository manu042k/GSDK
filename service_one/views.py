from rest_framework import viewsets # type: ignore
from .models import RandomModel
from .serializers import RandomModelSerializer
from rest_framework.permissions import AllowAny # type: ignore

# Create your views here.
class RandomModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RandomModel.objects.all()
    serializer_class = RandomModelSerializer

