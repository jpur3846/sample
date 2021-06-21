from rest_framework import generics
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer

class DataEndpoint(generics.GenericAPIView):
    permission_classes = []
    queryset = Data.objects.all()
    serializer_class = DataSerializer()
    
    def get(self, request):
        serializer = DataSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

