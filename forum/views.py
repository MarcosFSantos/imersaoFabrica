from django.shortcuts import render
from forum.models import Topico

# função view da página principal responsável por contruir a página de acordo com o banco de dados. 
def pagPrincipal(request):
    topicos = Topico.objects.all()
    data = {}
    data['topicos'] = topicos
    return render(request, 'pagPrincipal.html', data)