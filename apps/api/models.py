from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
from apps.users.models import CustomUser

from encrypted_model_fields.fields import EncryptedCharField
from .helpers.custom_upload import csv_upload_path
# Create your models here.

class ApiKey(models.Model):
    key = EncryptedCharField(max_length=255, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='api_keys')
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name}-{self.key}'

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.key[-6:]} {self.user.username}"

        super().save(*args, **kwargs)


class UploadFile(models.Model):
    csv_file = models.FileField(upload_to=csv_upload_path, max_length = 100)
    api_key = models.ForeignKey(ApiKey, on_delete=models.CASCADE, related_name='upload_files', null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    