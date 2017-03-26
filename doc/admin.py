from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin.helpers import ActionForm
from django import forms
from .models import Document, SaveLocation, Project, Collection
# Register your models here.


class DocumentResource(resources.ModelResource):
    class Meta:
        model = Document
        fields = ('number', 'date', 'summary', 'issued_by')
        import_id_fields = ('number', 'date')
        widgets = {
            'date': {'format': '%d/%m/%Y'},
        }


class DocumentAdminForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('__all__')
        widgets = {
            'date': admin.widgets.AdminDateWidget(format='%d/%m/%Y'),
        }


@admin.register(Document)
class DocumentAdmin(ImportExportModelAdmin):
    class BulkForm(ActionForm):
        value = forms.CharField(required=False)
        projects = forms.MultipleChoiceField(required=False, choices=[(p.pk, p.name) for p in Project.objects.all()])
        collections = forms.MultipleChoiceField(required=False, choices=[(c.pk, c.name) for c in Collection.objects.all()])

    form = DocumentAdminForm
    fieldsets = (
        (None, {
            'fields': ('number', 'date', 'issued_by', 'file')
        }),
        ('Options', {
            'classes': ('wide', ),
            'fields': ('summary', 'collections', 'projects')
        })
    )
    actions = ['bulk_edit_issued_by', 'bulk_edit_projects', 'bulk_edit_collections']
    action_form = BulkForm
    date_hierarchy = 'date'
    filter_horizontal = ('projects', 'collections')
    list_display = ('number', 'date', 'issued_by', 'summary', 'get_projects', 'file')
    list_filter = ('issued_by', 'projects')
    ordering = ['-date']
    resource_class = DocumentResource
    search_fields = ('number', 'date', 'issued_by', 'summary', 'projects__name')

    def get_projects(self, obj):
        return ", ".join([project.name for project in obj.projects.all()])
    get_projects.short_description = 'Dự án'

    def bulk_edit_issued_by(self, request, queryset):
        value = request.POST.get('value')
        queryset.update(issued_by=value)
    bulk_edit_issued_by.short_description = 'Update Nơi ban hành'

    def bulk_edit_projects(self, request, queryset):
        projects = request.POST.get('projects')
        for doc in queryset:
            for project in projects:
                doc.projects.add(projects)
    bulk_edit_projects.short_description = 'Update Dự án'

    def bulk_edit_collections(self, request, queryset):
        collections = request.POST.get('collections')
        for doc in queryset:
            for collection in collections:
                doc.collections.add(collection)
    bulk_edit_projects.short_description = 'Update Tập hồ sơ'


admin.site.register(SaveLocation)
admin.site.register(Project)
admin.site.register(Collection)
