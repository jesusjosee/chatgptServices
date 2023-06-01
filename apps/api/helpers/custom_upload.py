import os
from uuid import uuid4

def csv_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.csv_file}{uuid4().hex}.{ext}"
    return f'csv_files/{filename}'

