from django.shortcuts import render, redirect, HttpResponse
from .models import Patient
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PatientForm
from django.http import JsonResponse
from .serializers import RoutineSerarilizer
from rest_framework import viewsets
# from django.contrib.auth.mixins import LoginRequiredMixin

# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.values_list('routine', flat =True)
#     serializer_class = RoutineSerarilizer

def routine_list(request):
    name = Patient.objects.filter(name='Utsana').values()
    # print(dir(name))
    # print(f"time",name)
    serializer = RoutineSerarilizer(name, many= True)
    return JsonResponse({'Routine':serializer.data}, safe=False)

# def demo(request):
#     return JsonResponse({"message":"This is api call"})


# def routineAPI(request):
#     routine = Patient.objects.values_list('routine', flat =True)
#     serializer = RoutineSerarilizer(routine, many=True)
#     return JsonResponse(serializer.data, safe=False)


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = '/patient'
    template_name = 'patient/patient_delete.html'


class PatientUpdateView(SuccessMessageMixin, UpdateView):
    model = Patient
    success_url = '/patient'
    success_message = "Details Updated !"
    form_class = PatientForm


class PatientCreateView(SuccessMessageMixin, CreateView):
    model = Patient
    # fields = ['name','age','gender','contact','address','guardian_name','guardian_contact','medical_status','enroll']
    success_url = '/patient'
    success_message = "Patient Added !"
    form_class = PatientForm


class PatientListView(ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'patinet/patient_list.html'
    login_url = '/admin'
    success_url = '/patient'





class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'patient'

# def demo(request):
#     return JsonResponse({"message":"This is api call"})
   

    