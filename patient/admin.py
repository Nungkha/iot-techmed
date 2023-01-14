from django.contrib import admin
from .models import Patient
# Register your models here.


# class PatientAdmin(admin.ModelAdmin):
#     list_display = ['name','age','gender','contact','address','guardian_name','guardian_contact','timestamp']


admin.site.register(Patient)