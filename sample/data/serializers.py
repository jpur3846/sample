from .models import Data
from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    class Meta:
        model = Data