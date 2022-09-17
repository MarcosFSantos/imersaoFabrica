from django.shortcuts import render, redirect
from forum.models import Topico, Comentario
from forum.forms import TopicoForm

# Função view da página principal, responsável por contruir a página de acordo com o banco de dados. 
def pagPrincipal(request):
    topicos = Topico.objects.all() # 
    data = {}
    data['topicos'] = topicos
    return render(request, 'pagPrincipal.html', data)

# Função view da página de detalhe de um tópico, específico responsável por construir a página de acordo com o banco de dados.
def pagTopico(request, pk):
    topico = Topico.objects.get(pk=pk) # Cria uma instancia do tópico presente no banco de dados que tem a chave primária(id) especificada na url.
    data = {}
    data['topico'] = topico
    return render(request, 'pagTopico.html', data)

# Função view da página de criação de tópico, responsável por construir a página de acordo com o banco de dados.
def pagCriarTopico(request):
    form = TopicoForm(request.POST or None)

    # Verifica se o formulário é valido, e salva o formulário caso ele seja.
    if form.is_valid():
        form.save()
        return redirect('principal')
    data = {}
    data['form'] = form
    return render(request, 'pagCriarTopico.html', data)

# Função view da página de atualização de tópico, reponsável por construir a página de acordo com o banco de dados.
def pagAtualizarTopico(request, pk):
    topico = Topico.objects.get(pk=pk)
    form = TopicoForm(request.POST or None, instance= topico)

    # Verifica se o formulário é válido
    if form.is_valid():
        form.save()
        return redirect('principal')
    data = {}
    data['topico'] = topico
    data['form'] = form
    return render(request, 'pagAtualizarTopico.html', data)

# Função view responsável pela exclusão de um tópico.
def pagDeletarTopico(request, pk):
    topico = Topico.objects.get(pk=pk)
    topico.delete()
    return redirect('principal')