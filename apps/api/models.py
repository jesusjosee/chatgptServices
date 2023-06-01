from django.db import models
from .helpers.custom_upload import csv_upload_path
# Create your models here.

class UploadFile(models.Model):
    csv_file = models.FileField(upload_to=csv_upload_path, max_length = 100)
    