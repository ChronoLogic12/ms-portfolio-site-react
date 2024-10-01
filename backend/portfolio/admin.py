from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
            'title', 'description', 'live_site_url', 'git_repository_url', 
            'year', 'background_image', 'technologies', 'position'
        )
    list_editable = ('position',)
    ordering = ('position',)


admin.site.register(Project, ProjectAdmin)