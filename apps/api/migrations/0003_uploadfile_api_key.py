# Generated by Django 4.2.1 on 2023-06-03 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_apikey'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='api_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upload_files', to='api.apikey'),
        ),
    ]
