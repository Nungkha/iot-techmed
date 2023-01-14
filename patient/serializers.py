from rest_framework import serializers
from .models import Patient


class RoutineSerarilizer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['routine'] 