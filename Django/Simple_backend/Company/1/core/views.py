# core/views.py
from rest_framework import generics
from .models import HomePage, AboutUs, Contact, ContactForm, Carousel 
from .serializers import HomePageSerializer, AboutUsSerializer, ContactSerializer, ContactFormSerializer,CarouselSerializer

class HomePageListCreate(generics.ListCreateAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer

class HomePageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer

class CarouselListCreat(generics.ListCreateAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer

class AboutUsListCreate(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class AboutUsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactFormListCreate(generics.ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class ContactFormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
