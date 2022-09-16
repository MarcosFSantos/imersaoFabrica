from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def bomDia(request):
    texto = "<html><body><h1>Bom dia!!!</h1></body></html>"
    return HttpResponse(texto)

def boaNoite(request):
    texto = "<html><body><h1>Boa noite!!!</h1></body></html>"
    return HttpResponse(texto)

def home(request):
    return render(request, template_name='home.html')