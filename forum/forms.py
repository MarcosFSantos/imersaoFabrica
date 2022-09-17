from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from forum.models import Topico, Comentario

# Formulário utilizado para criação de um tópico.
class TopicoForm(ModelForm):
    class Meta:
        model = Topico
        fields = ['titulo', 'autor', 'conteudo']

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'conteudo', 'topico']