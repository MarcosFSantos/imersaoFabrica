from django.shortcuts import render

def pagPrincipal(request):
    return render(request, 'pagPrincipal.html')