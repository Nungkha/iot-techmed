from django import forms
from django.contrib.admin.widgets import AdminTimeWidget, AdminDateWidget
from .models import Patient



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        # fields = ('name','age','gender','contact','address','guardian_name','guardian_contact')
        fields = "__all__"
        widgets = {
            "routine" : AdminTimeWidget(),
        }

    