# core/urls.py
from django.urls import path
from .views import (
    HomePageListCreate, HomePageDetail,
    AboutUsListCreate, AboutUsDetail,
    ContactListCreate, ContactDetail,
    ContactFormListCreate, ContactFormDetail,
    CarouselListCreat
)

urlpatterns = [
    path('home/', HomePageListCreate.as_view(), name='home-list-create'),
    path('home/<int:pk>/', HomePageDetail.as_view(), name='home-detail'),
    path('about/', AboutUsListCreate.as_view(), name='about-list-create'),
    path('about/<int:pk>/', AboutUsDetail.as_view(), name='about-detail'),
    path('contact/', ContactListCreate.as_view(), name='contact-list-create'),
    path('contact/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
    path('contact-form/', ContactFormListCreate.as_view(), name='contact-form-list-create'),
    path('carousel/', CarouselListCreat.as_view(), name='CarouselListCreat'),
    path('contact-form/<int:pk>/', ContactFormDetail.as_view(), name='contact-form-detail'),
]