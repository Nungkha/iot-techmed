from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    enroll = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)

    Male = 'M'
    Female = 'F'
    gender = [
        (Male, 'Male'),
        (Female, 'Female'),
    ]
    gender = models.CharField(
        max_length=2,
        choices=gender,
        default=Male,
    )
    contact = models.BigIntegerField()
    address = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=100)
    guardian_contact = models.BigIntegerField()
    medical_status = models.TextField(blank=True, null=True)
    medicine = models.CharField(max_length=100, blank=True, null=True)
    medicine_description = models.TextField(blank=True, null=True)
    routine = models.TimeField(auto_now_add=False, blank=True, null=True)
    dose = models.IntegerField(default='0')

    def __str__(self):
        return self.name



# class Medicine(models.Model):
#     medName = models.CharField(max_length=100)
#     medStatus = models.TextField(null=True, blank=True )
#     routine = models.DateTimeField()


# class Prescription(models.Model):
#     medical_status = models.TextField()
#     medicine = models.CharField(max_length=100)
#     medicine_description = models.TextField()
#     routine = models.DateTimeField()
#     dose = models.IntegerField()