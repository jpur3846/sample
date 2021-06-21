from rest_framework import generics
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer

class DataEndpoint(generics.GenericAPIView):
    queryset = Data.objects.all()
    
    def get(self, request):
        serializer = DataSerializer(self.get_queryset())
        return Response(serializer.data)

