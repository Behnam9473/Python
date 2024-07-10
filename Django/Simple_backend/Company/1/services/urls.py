# urls.py (در پوشه اپلیکیشن شما)

from django.urls import path
from .views import ServicesListCreate, ServicesRetrieveUpdateDestroy

urlpatterns = [
    path('', ServicesListCreate.as_view(), name='company-list-create'),
    path('<int:pk>/', ServicesRetrieveUpdateDestroy.as_view(), name='company-detail'),
]