# urls.py (در پوشه اپلیکیشن شما)

from django.urls import path
from .views import CompanyListCreate, CompanyRetrieveUpdateDestroy

urlpatterns = [
    path('', CompanyListCreate.as_view(), name='company-list-create'),
    path('<int:pk>/', CompanyRetrieveUpdateDestroy.as_view(), name='company-detail'),
]