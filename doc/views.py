from django.views.generic.detail import DetailView
from django_tables2 import SingleTableView
from .models import Document, Project
from .tables import DocumentTable
# Create your views here.


class DocListView(SingleTableView):
    model = Document
    table_class = DocumentTable



class ProjectDetailView(DetailView):
    model = Project


class DocumentDetailView(DetailView):
    model = Document
