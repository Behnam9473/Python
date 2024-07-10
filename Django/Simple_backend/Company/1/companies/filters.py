# filters.py
import django_filters
from .models import Companies

class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')
    state = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Companies
        fields = ['name', 'city', 'state']
