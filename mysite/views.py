from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Strona Główna<br>'
    '<a href=/polls/>Przejrzyj pytania</a><br>'
    '<a href=/admin/>panel administratora</a>')