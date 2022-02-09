from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    preview_image = models.CharField(max_length=100)
    github_url = models.CharField(max_length=100)
    deployed_url = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)