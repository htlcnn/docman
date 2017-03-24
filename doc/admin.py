from django.contrib import admin
from django import forms
from .models import Document, SaveLocation, Project, Collection
# Register your models here.


class DocumentAdminForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('__all__')
        widgets = {
            'date': admin.widgets.AdminDateWidget(format='%d/%m/%Y'),
        }


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    form = DocumentAdminForm
    filter_horizontal = ('projects', 'collections')


admin.site.register(SaveLocation)
admin.site.register(Project)
admin.site.register(Collection)

