from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def index(request):
    return HttpResponse('Strona Główna<br>'
    '<a href=/polls/>Przejrzyj pytania</a><br>'
    '<a href=/admin/>panel administratora</a>')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"