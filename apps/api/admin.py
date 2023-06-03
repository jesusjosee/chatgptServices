from django.contrib import admin
from .models import UploadFile, ApiKey
# Register your models here.

@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):
    pass

@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    pass