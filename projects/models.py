from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    #link = models.FilePathField(allow_folders=True)

    def __str__(self):
        return self.title
