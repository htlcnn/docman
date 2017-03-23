from django.contrib import admin
from django import forms
from .models import Doc, SaveLocation
# Register your models here.


class DocAdminForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y', ], widget=forms.DateInput)

    class Meta:
        model = Doc
        fields = ['no', 'date', 'summary', 'issued_by', 'location', 'tags']


@admin.register(Doc)
class DocAdmin(admin.ModelAdmin):
    list_display = ('no', 'date', 'summary', 'issued_by', 'location')
    form = DocAdminForm


admin.site.register(SaveLocation)

