from django.db import models
from apps.users.models import CustomUser

from encrypted_model_fields.fields import EncryptedCharField
from .helpers.custom_upload import csv_upload_path
# Create your models here.

class ApiKey(models.Model):
    key = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='api_keys')
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Apikey de {self.name}'

    def save(self, *args, **kwargs):
        if not self.name:
            username = self.user.email.split('@')[0]
            self.name = f"{username}-{self.key[-6:]}"
        
        if not ApiKey.objects.filter(key=self.key, user=self.user).exists():
            super().save(*args, **kwargs)

    def get_last_upload_file(self):
        try:
            return self.upload_files.latest('id')
        except UploadFile.DoesNotExist:
            return None

class UploadFile(models.Model):
    csv_file = models.FileField(upload_to=csv_upload_path, max_length = 100)
    api_key = models.ForeignKey(ApiKey, on_delete=models.CASCADE, related_name='upload_files', null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    