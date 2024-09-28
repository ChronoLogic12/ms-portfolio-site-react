from django.db import models

TECHNOLOGIES_CHOICES = [
    ("html", "html"),
    ("css", "css"),
    ("javascript", "javascript"),
    ("python", "python"),
    ("django", "django"),
    ("react", "react"),
    ("stripe", "stripe"),
]

class Project(models.Model):
    title = models.CharField(max_length = 128)
    description = models.CharField(max_length = 1024)
    live_site_url = models.CharField(max_length = 1024)
    git_repository_url = models.CharField(max_length = 1024)
    year = models.CharField(max_length = 4)
    background_image = models.ImageField()
    technologies = models.CharField(choices=TECHNOLOGIES_CHOICES)
    position = models.IntegerField(max_length=2, unique=True)

def __str__(self):
    return self.title
