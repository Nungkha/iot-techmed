# Generated by Django 4.1.3 on 2022-12-22 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patient_year_in_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='contact',
            new_name='contact_hello',
        ),
    ]
