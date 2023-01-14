from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from patient.models import Patient
from django.contrib.auth.views import LoginView, LogoutView


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_content = {}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url='/admin'


def search(request):
    query = request.GET['query']
    searchedPatient = Patient.objects.filter(name__icontains=query)
    params = {'searchedPatient':searchedPatient}
    print(params)
    return render(request, 'home/search.html', params)