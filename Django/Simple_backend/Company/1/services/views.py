from rest_framework import generics
from .models import Services
from .serializers import ServicesSerializer


class ServicesListCreate(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class ServicesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer