# Generated by Django 4.1.3 on 2023-01-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_patient_dose_patient_enroll_patient_medicine_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='refil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
