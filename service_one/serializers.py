from rest_framework import serializers
from .models import RandomModel

class RandomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomModel
        fields = '__all__'