from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order']
    list_editable = ['featured', 'order']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'featured']
    search_fields = ['title', 'description']