from django.conf.urls import url
from doc import views

app_name = 'doc'

urlpatterns = [
    url(r'^$', views.DocListView.as_view(), name='doc-list'),
    url(r'^doc/(?P<pk>[0-9]+)/$', views.DocumentDetailView.as_view(), name='document-detail'),
    url(r'^project/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
]
