from django.contrib import admin
from management.models import Project  

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'client', 'created_at', 'updated_at', 'release_date')
    list_filter = ('name',)
    search_fields = ('name', 'client')
    
admin.site.register(Project, ProjectAdmin)