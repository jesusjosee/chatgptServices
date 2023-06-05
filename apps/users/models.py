from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField( _('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email   
    
    def get_api_key(self):
        from apps.api.models import ApiKey 
        try:
            return self.api_keys.latest('id').key
        except ApiKey.DoesNotExist:
            return None
        
    def get_last_csv_file(self):
        from apps.api.models import ApiKey, UploadFile
        try:
            api_key = self.api_keys.latest('id')
            return api_key.upload_files.latest('id').csv_file
        except (ApiKey.DoesNotExist, UploadFile.DoesNotExist):
            return None
