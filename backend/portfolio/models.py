from django.db import models
from multiselectfield import MultiSelectField

TECHNOLOGIES_CHOICES = (
    ("html", "html"),
    ("css", "css"),
    ("javascript", "javascript"),
    ("python", "python"),
    ("django", "django"),
    ("react", "react"),
    ("stripe", "stripe"),
)

class Project(models.Model):
    title = models.CharField(max_length = 128)
    description = models.CharField(max_length = 1024, default="")
    live_site_url = models.CharField(max_length = 1024)
    git_repository_url = models.CharField(max_length = 1024)
    year = models.CharField(max_length = 4)
    background_image = models.ImageField(upload_to='images/')
    technologies = MultiSelectField(choices=TECHNOLOGIES_CHOICES)
    position = models.PositiveIntegerField(unique=True, default=999)

def __str__(self):
    return self.title

class Meta:
        ordering = ['position']
