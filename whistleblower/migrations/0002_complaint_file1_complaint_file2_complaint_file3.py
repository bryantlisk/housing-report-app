# Generated by Django 4.2.10 on 2024-03-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whistleblower', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='file1',
            field=models.FileField(blank=True, null=True, upload_to='report_files'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='report_files'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='file3',
            field=models.FileField(blank=True, null=True, upload_to='report_files'),
        ),
    ]
