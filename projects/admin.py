from django.contrib import admin
from django import forms
from django.utils.html import format_html, format_html_join
from ckeditor.widgets import CKEditorWidget
from .models import Project

class ProjectAdminForm(forms.ModelForm):
    impact = forms.CharField(widget=CKEditorWidget())
    features = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Project
        fields = '__all__'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

    list_display = ['title', 'category', 'featured', 'short_impact', 'tech_tags', 'order']
    list_editable = ['featured', 'order']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'featured']
    search_fields = ['title', 'description', 'impact', 'features']

    def short_impact(self, obj):
        return obj.impact[:60] + "..." if len(obj.impact) > 60 else obj.impact
    short_impact.short_description = "Impact du projet"

    def tech_tags(self, obj):
        if not obj.technologies:
            return "-"
        tags = obj.technologies.split(',')
        return format_html(
            format_html_join(
                '',
                '<span style="display:inline-block; background:#0dcaf0; color:#fff; border-radius:4px; padding:2px 6px; margin:2px; font-size:0.8rem;">{}</span>',
                ((tag.strip(),) for tag in tags)
            )
        )
    tech_tags.short_description = "Technologies"