# Generated by Django 4.1.3 on 2022-12-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_patient_medical_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dose',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='patient',
            name='enroll',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='medicine',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='medicine_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='routine',
            field=models.TimeField(blank=True, null=True),
        ),
    ]