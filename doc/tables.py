import django_tables2 as tables
from django_tables2.utils import A
from .models import Document


class DocumentTable(tables.Table):

    number = tables.LinkColumn('doc:document-detail', args=[A('pk')])

    class Meta:
        model = Document
        fields = ('number', 'date', 'summary', 'issued_by', 'projects')
        attrs = {'class': 'table-striped table-bordered table-hover'}
        empty_text = 'No content'
        per_page = 100

