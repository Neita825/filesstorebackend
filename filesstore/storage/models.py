from django.db import models

class File(models.Model):
    url = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="UploadedFiles/")
    user = models.IntegerField(null=True)
    fileName = models.CharField(max_length=200, null=True)
    revision = models.IntegerField(null=True)