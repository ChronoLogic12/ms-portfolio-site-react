from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'title', 'description', 'live_site_url', 'git_repository_url', 
            'year', 'background_image', 'technologies', 'position'
        )