from rest_framework import generics
from .models import Companies
from .serializers import CompanySerializer

class CompanyListCreate(generics.ListCreateAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer

class CompanyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
