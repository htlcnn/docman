import django_filters
from .models import Document


class DocumentListFilter(django_filters.FilterSet):

    class Meta:
        model = Document
        fields = {
            'number': ['icontains'],
            'date': ['gt', 'lt'],
            'summary': ['icontains'],
            'issued_by': ['icontains'],
        }
